import datetime
months = {"JANUARY": 1, "FEBRUARY": 2, "MARS": 3, "APRIL": 4, "MAY": 5, "JUNE": 6, "JULY": 7, "AUGUST": 8, "SEPTEMBER": 9, "OCTOBER": 10, "NOVEMBER": 11, "DECEMBER": 12}
months_with_31_days = {"JANUARY": 1, "MARS": 3,  "MAY": 5, "JULY": 7, "AUGUST": 8, "OCTOBER": 10, "DECEMBER": 12}
months_with_30_days = {"APRIL":4, "JUNE": 6, "SEPTEMBER": 9, "NOVEMBER": 11}

months_with_31_days_numbers = [1, 3, 5, 7, 8, 10, 12]
months_with_30_days_numbers = [4, 6, 9, 11]


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
    if month.isnumeric() and int(month) in months_with_31_days_numbers and day.isnumeric() and int(day) >= 1 and int(day) <= 31:
        return True
    
    elif month.isnumeric() and int(month) in months_with_30_days_numbers and day.isnumeric() and int(day) >= 1 and int(day) <= 30:
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
    
        
        
#Skottår
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
 
def leapyear_number(year, month,day):
    if int(year) % 4 == 0 and month.isnumeric() and int(month) == 2 and day_leapyear(day):
        return True
    
    else:
        return False



    
#Fråga efter ett datum
def date():
    while True:
        (year,month,day) = (input("Year (Now-2099): "), input("Month (January-December) or (01-12): "), input("Day: "))
        if correct_year(year) and (day_in_month(month, day) or leapyear_string(year, month, day)):
            dateWT = datetime.datetime(int(year), months[month.upper()], int(day))
            dateWOT = dateWT.date()
            if correct_date(dateWOT):
                break
            
            else:
                print()
                print("Date has already passed")
                print()
            
        
        elif correct_year(year) and (day_in_month_number(month, day) or leapyear_number(year, month,day)):
            dateWT = datetime.datetime(int(year), int(month), int(day))
            dateWOT = dateWT.date()
            if correct_date(dateWOT):
                break
            
            else:
                print()
                print("Date has already passed")
                print()
        else:
            print()
            print("Invalid date")
            print()
    
    return dateWOT
        
       
def menu(title, prombt, options):
    print(title)
    print()
    for x in options:
        print(f"   {x}) {options[x]}")
    print()
    while True:
        fråga = input(prombt)
        if fråga in options:
            break
    return fråga 
    print()

def listx():
    emptylist = []
    return emptylist

#Lägg till en aktivitet kopplat till ett datum
def add_activities():
    list_with_dates = listx()
    while True:
        options = {"y":"Yes", "n":"No"} 
        question = menu("Do you want to add an activity?", "[y/n]: ", options)
        list_with_dates.sort()
        if question == "y":
            print()
            act = input("What activity do you want to add?: ")
            print()
            print()
            print("When is the activity?")
            print()
            dat = date()
            list_with_dates.append((dat, act))
            print()
            
            
        elif question == "n":
            print()
            print()
            print("Your activities:")
            print()
            for x in range(len(list_with_dates)):
                dat, act = list_with_dates[x] 
                print(f"  {x+1}) {dat}: {act}")
            return list_with_dates
            break

#Lägg till en activitet till din lista
def add_act(xs):
    print()
    act = input("What activity do you want to add?: ")
    print()
    print()
    print("When is the activity?")
    print()
    dat = date()
    xs.append((dat, act))
    xs.sort()
    print()
    print()
    print("Your activities:")
    print()
    for x in range(len(xs)):
        dat, act = xs[x]
        print(f"  {x+1}) {dat}: {act}")
    print()




#Ta bort en aktivitet från din lista
def remove_act(xs):
    if xs == []:
        print()
        print("List is empty")
    
    elif len(xs) == 1:
        print()
        print("Do you want to remove your last activity?")
        rem1 = menu("", "[y/n]: ", options)
        if rem1 == "y":
            xs.remove(xs[0])
        print()
        print("Your activities:")
        print()
        xs.sort()
        for x in range(len(xs)):
            dat, act = xs[x]
            print(f"  {x+1}) {dat}: {act}")
        
        
    else:
        print()
        for x in range(len(xs)):
            dat, act = xs[x]
            print(f"  {x+1}) {dat}: {act}")
        print()
        print("What activity do you want to remove?")
        print()
        while True:
            rem = input(f"(1-{len(xs)}): ")
            if rem.isnumeric() and int(rem) >= 1 and int(rem) <= (len(xs)):
                xs.remove(xs[int(rem)-1])
                print()
                print("Your activities")
                print()
                for x in range(len(xs)):
                    dat, act = xs[x]
                    print(f"  {x+1}) {dat}: {act}")
                break
                
    
    
    

opt = {"a":"Add activity", "r":"Remove activity"}
def edit_list(xs):
    print()
    aor = menu("Edit list", "Option: ", opt)
    if aor == "a":
        add_act(xs)
    elif aor == "r":
        remove_act(xs)
    
    
    
    


def create_and_edit_list():
    datelist = add_activities()
    while True:
        edit_list(datelist)
    
    
    
    
    
create_and_edit_list() 



    
    




    


