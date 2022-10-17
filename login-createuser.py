import json
import sys
import os

def default(filepath):
    if not os.path.exists(filepath):
        file = open(filepath, 'x')
        file.write("{}")
        file.close()

def write(filepath, dictionary):
    with open(filepath,"w") as f:
        f.writelines(json.dumps(dictionary))

def read(filepath):
    file = open(filepath,"r")
    return json.loads(file.read())

def menu(title,prompt,options):
    print(title)
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
    sys.exit(0)
            
def login(users):
    loggedOut = True
    while loggedOut:
        #Alternativ skapa användare/ logga in befintlig användare
        login = {"l":"Log into existing user", "c":"Create new user", "d":"Delete user", "q":"Quit"}
        lgn = menu("", "", login)
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
            while True:
                print()
                print("Create new user")
                print()
                user = input("Choose a username: ")
                print()
                if user in users:
                    print("Username already taken.")
                    break
                else:
                    users[user] = input("Choose a password: ")
                    print()
                    userList[user] = []
                    break
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
def run():
    default("users.txt")
    default("userlist.txt")
    global users
    global userList
    users = read("users.txt")
    userList = read("userlist.txt")
    user = login(users)

run()              