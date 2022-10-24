import datetime
import json
import sys
import os

months = {"JANUARY": 1, "FEBRUARY": 2, "MARS": 3, "APRIL": 4, "MAY": 5, "JUNE": 6, "JULY": 7, "AUGUST": 8,
          "SEPTEMBER": 9, "OCTOBER": 10, "NOVEMBER": 11, "DECEMBER": 12}

months_with_31_days = {"JANUARY": 1, "MARS": 3, "MAY": 5, "JULY": 7, "AUGUST": 8, "OCTOBER": 10, "DECEMBER": 12}
months_with_30_days = {"APRIL": 4, "JUNE": 6, "SEPTEMBER": 9, "NOVEMBER": 11}

months_with_31_days_numbers = [1, 3, 5, 7, 8, 10, 12]
months_with_30_days_numbers = [4, 6, 9, 11]


def default(filepath):
    if not os.path.exists(filepath):
        file = open(filepath, 'x')
        file.write("{}")
        file.close()


def write(filepath, userlist: dict):
    with open(filepath, "w") as f:
        f.writelines(json.dumps(userlist))


def read(filepath):
    file = open(filepath, "r")
    return json.loads(file.read())


def dateToDict(d):
    val = {}

    val["year"] = d.year
    val["month"] = d.month
    val["day"] = d.day

    return val


def dictToDate(dic):
    return datetime.date(dic["year"], dic["month"], dic["day"])

def save_data():
    savelist = []
    for val in userList[user]:
        dat, act = val
        savelist.append((dateToDict(dat), act))
    userList[user] = savelist
    write("users.txt", users)
    write("userlist.txt", userList)


def translate_list():
    translate_list = []
    for val in userList[user]:
        dic, act = val
        translate_list.append((dictToDate(dic), act))
    userList[user] = translate_list
    return userList[user]



def day_in_month(month, day):
    if month.upper() in months_with_31_days and day.isnumeric() and int(day) >= 1 and int(day) <= 31:
        return True

    elif month.upper() in months_with_30_days and day.isnumeric() and int(day) >= 1 and int(day) <= 30:
        return True

    elif month.upper() == "FEBRUARY" and int(day) >= 1 and int(day) <= 28:
        return True

    else:
        return False


def day_in_month_number(month, day):
    if month.isnumeric() and int(month) in months_with_31_days_numbers and day.isnumeric() and int(day) >= 1 and int(
            day) <= 31:
        return True

    elif month.isnumeric() and int(month) in months_with_30_days_numbers and day.isnumeric() and int(day) >= 1 and int(
            day) <= 30:
        return True

    elif month.isnumeric() and int(month) == 2 and day.isnumeric() and int(day) >= 1 and int(day) <= 28:
        return True

    else:
        return False


def correct_year(year):
    if year.isnumeric() and int(year) <= 2099:
        return True
    else:
        return False


def today():
    today = datetime.datetime.now()
    todaysdate = today.date()
    return todaysdate


def correct_date(date):
    passed = date - today()
    if passed.days >= 0:
        return True
    else:
        return False


# Skottår
def day_leapyear(day):
    if day.isnumeric() and int(day) == 29:
        return True
    else:
        return False


def leapyear_string(year, month, day):
    if int(year) % 4 == 0 and month.upper() == "FEBRUARY" and day_leapyear(day):
        return True

    else:
        return False


def leapyear_number(year, month, day):
    if int(year) % 4 == 0 and month.isnumeric() and int(month) == 2 and day_leapyear(day):
        return True

    else:
        return False


# Fråga efter ett datum
def date():
    while True:
        (year, month, day) = (
            input("Year (Now-2099): "), input("Month (January-December) or (01-12): "), input("Day: "))
        if correct_year(year) and (day_in_month(month, day) or leapyear_string(year, month, day)):
            date = datetime.date(int(year), months[month.upper()], int(day))
            if correct_date(date):
                break

            else:
                print()
                print("Date has already passed")
                print()


        elif correct_year(year) and (day_in_month_number(month, day) or leapyear_number(year, month, day)):
            date = datetime.date(int(year), int(month), int(day))
            if correct_date(date):
                break

            else:
                print()
                print("Date has already passed")
                print()
        else:
            print()
            print("Invalid date")
            print()

    return date


def activities():
    while True:
        acts = input("What activity do you want to add?: ")
        if len(acts) > 100:
            print()
            print("Activity can´t be longer than 100 characters")
            print()
        elif acts.split() == []:
            print()
            print("You need to add an activity")
            print()
        else:
            return acts


def menu(title, prombt, options):
    print(title)
    print()
    for x in options:
        print(f"   {x}) {options[x]}")
    print()
    while True:
        question = input(prombt)
        if question in options:
            break
    return question


def print_activities(xs):
    if xs == []:
        print("You have no list saved to this user")
        print()
    else:
        print("Your activities:")
        print()
        for x in range(len(xs)):
            dat, act = xs[x]
            print(f"  {x + 1}) {dat}: {act}")
        print()


# Lägg till en aktivitet kopplat till ett datum
def add_activities(xs):
    while True:
        options = {"y": "Yes", "n": "No"}
        question = menu("Do you want to add an activity?", "[y/n]: ", options)
        if question == "y":
            print()
            act = activities()
            print()
            print()
            print("When is the activity?")
            print()
            dat = date()
            xs.append((dat, act))
            print()


        elif question == "n":
            print()
            xs.sort()
            print()
            print_activities(xs)
            return xs


# Lägg till en activitet till din lista
def add_act(xs):
    print()
    act = activities()
    print()
    print()
    print("When is the activity?")
    print()
    dat = date()
    xs.append((dat, act))
    xs.sort()
    print()
    print()
    print_activities(xs)
    print()


# Ta bort en aktivitet från din lista
def remove_act(xs):
    if xs == []:
        print()
        print("List is empty")

    elif len(xs) == 1:
        print()
        print("Do you want to remove your last activity?")
        options = {"y": "Yes", "n": "No"}
        rem1 = menu("", "[y/n]: ", options)
        if rem1 == "y":
            xs.remove(xs[0])
        print()

    else:
        print()
        print_activities(xs)
        print()
        print("What activity do you want to remove?")
        print()
        while True:
            rem = input(f"(1-{len(xs)}): ")
            if rem.isnumeric() and int(rem) >= 1 and int(rem) <= (len(xs)):
                xs.remove(xs[int(rem) - 1])
                print()
                print_activities(xs)
                break


def edit_list(xs):
    print_activities(xs)
    while True:
        if xs == []:
            break
        opt = {"a": "Add activity", "r": "Remove activity", "b": "Back to menu"}
        aor = menu("Edit list", "Option: ", opt)
        if aor == "a":
            add_act(xs)
        elif aor == "r":
            remove_act(xs)
        elif aor == "b":
            print()
            break


def quit():
    print()
    print("Shutting down...")
    write("users.txt", users)
    write("userlist.txt", userList)
    sys.exit(0)


def login(users):
    loggedOut = True
    while loggedOut:
        # Alternativ skapa användare/ logga in befintlig användare
        login = {"l": "Log into existing user", "c": "Create new user", "d": "Delete user", "q": "Quit"}
        lgn = menu("Choose an action", "Option: ", login)
        if lgn == 'l':
            while True:
                # Tar användarens input i form av inloggningsuppgifter
                if users == {}:
                    print()
                    print("No users exists")
                    print()
                    break
                print()
                user = input("User: ")
                password = input("Password: ")
                print()
                # Godkänd input
                if user in users and password == users[user]:
                    loggedOut = False
                    print()
                    print(f"Welcome {user}")
                    return user
                # Felaktig input
                if loggedOut:
                    options = {"r": "Try again", "b": "Back to main menu"}
                    opt = menu("Invalid username or password", "Option: ", options)
                    if opt == 'b':
                        print()
                        break

        # Skapa ny användare med tillhörande lista
        elif lgn == 'c':
            while True:
                print()
                print("Create new user")
                print()
                user = input("Choose a username: ")
                if user in users:
                    print("Username already taken.")
                    break
                else:
                    users[user] = input("Choose a password: ")
                    print()
                    userList[user] = []
                    write("users.txt", users)
                    write("userlist.txt", userList)
                    break
        # Ta bort användare
        elif lgn == 'd':
            print()
            if users == {}:
                print("No users exist")
                print()

            else:
                print("Users: *")
                print()
                for _ in users:
                    print(f"* {_}")
                print()
                user = input("Select a user to remove: ")
                if user in users:
                    password = input(f"Enter the password for user {user}: ")
                    while True:
                        if password == users[user]:
                            del (users[user])
                            del (userList[user])
                            print()
                            print(f"User {user} removed successfully.")
                            print()
                            write("users.txt", users)
                            write("userlist.txt", userList)
                            break
                        else:
                            print()
                            print(f"Incorrect password for user {user}.")
                            print()
                            break

                else:
                    print(f"User {user} does not exist.")
                    print()

        elif lgn == 'q':
            quit()
            loggedOut = False


def create_or_edit_list(user, xs):
    print_activities(xs)
    while True:
        if xs == []:
            options1 = {"c": "Create new list", "s": "Save and log out"}
            question = menu("Choose an action", "Option: ", options1)
            if question == "c":
                print()
                xs.clear()
                xs = add_activities(xs)

            elif question == "s":
                save_data()
                print()
                break

        else:
            options2 = {"c": "Create new list", "e": "Edit list", "s": "Save and log out"}
            question = menu("Choose an action", "Option: ", options2)
            if question == "c":
                print()
                xs.clear()
                xs = add_activities(xs)

            elif question == "e":
                print()
                edit_list(xs)
                print_activities(xs)

            elif question == "s":
                save_data()
                print()
                break
            
            
def run():
    default("users.txt")
    default("userlist.txt")
    global users
    global userList
    global user
    users = read("users.txt")
    userList = read("userlist.txt")
    print("Welcome to plan-your-day")
    print()
    while True:
        user = login(users)
        translate_list()
        print()
        if user == "q":
            break
        create_or_edit_list(user, userList[user])


run()

