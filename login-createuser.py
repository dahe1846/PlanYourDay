import json
import sys

def write(file, dictionary):
    with open(file,"w") as f:
        f.writelines(json.dumps(dictionary))

def read(file):
    file = open(file,"r")
    return json.loads(file.read())

users = read("users.txt")
userList = read("userlist.txt")

def menu(title,prompt,options):
    print(title)
    print()
    for option in options:
        print(f" {option}) {options[option]}")
    print()
    while True:
        s = input(f"{prompt} ")
        for option in options: 
            if s == (option) :
                return option
            
def quit():
    print("Shutting down...")
    write("users.txt", users)
    write("userlist.txt", userList)
    sys.exit("Program terminated")
            
def login(users):
    loggedOut = True
    while loggedOut:
        #Alternativ skapa användare/ logga in befintlig användare
        login = {"l":"Log into existing user", "c":"Create new user", "d":"Delete user", "q":"Quit"}
        lgn = menu("Log in", "", login)
        if lgn == 'l':
            while True:
                #Tar användarens input i form av inloggningsuppgifter
                user = input("User: ")
                password = input("Password: ")
                print()
                #Godkänd input
                if user in users and password == users[user] :
                    loggedOut = False
                    print(f"Welcome {user}")
                    return user
                #Felaktig input
                if loggedOut:
                    print("Invalid username or password")
                    options = {"r":"Try again", "b":"Back to main menu"}
                    opt= menu("", "", options)
                    print(f"Option: {opt}")
                    if opt == 'b' :
                        break
                        
        #Skapa ny användare med tillhörande lista
        elif lgn == 'c':
            print()
            print("Create new user")
            print()
            user = input("Choose a username: ")
            users[user] = input("Choose a password: ")
            print()
            userList[user] = []
        #Ta bort användare
        elif lgn == 'd':
            print()
            for _ in users:
                print(f"* {_}")
            print()
            user = input("Select a user to remove: ")
            print()
            if user in users:
                password = input(f"Enter the password for user {user}: ")
                while True:
                    if password == users[user]:
                        del(users[user])
                        del(userList[user])
                        print()
                        print(f"User {user} removed successfully.")
                        print()
                        break
                    else:
                        print()
                        print(f"Incorrect password for user {user}.")
                        print()
                        break
                    
            else:
                print(f"User {user} does not exist.")
                
        elif lgn == 'q':
            quit()
            loggedOut = False
                
user = login(users)