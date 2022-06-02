# All the imports needed
import os
import time
import random
# The sorting hat function 
def Sorting_Hat():
    Sorting = input("What is your name?: ")
    # The random number
    if Sorting == 'Alec':
        print('Ah hello')
        print("Hmm you might belong in...")
        num = random.randint(1,4)
        # The houses 
        print(num)
        if num == 1:
            print("You are in...Gryffindor! ")
            time.sleep(1)
            print ("Ah Gryffindor!. The bravest of the houses, also the house of the once great Albus Dumbledore!")
        elif num == 2:
            print("You are in...Hufflepuff! ")
            time.sleep(1)
            print("Ah Hufflepuff!. The most humble of the houses, also the house of Helga Hufflepuff!, the houses founder")
        elif num == 3:
            print("You are in...Ravenclaw! ")
            time.sleep(1)
            print("Ah Ravenclaw!. The most clever of the houses, also the house of the amazing Luna Lovegood! ")
        elif num == 4:
            print("You are in...Slytherin!")
            time.sleep(1)
            print("Ah Slytherin...the most evil of the houses, home to Tom Marvolo Riddle or also known as He who must not be named... ")
# The addition function
def Add_Number():
    number1 = input("Enter the first number: ")
    number2 = input("Enter the last number: ")
    Sum = int(number1) + int(number2)
    print(Sum)
# The birthdate challenge 
def birthdate():
    import datetime
    currentDate = datetime.datetime.now()
    deadline = input ('Please enter your date of birth: ')
    deadlineDate = datetime.datetime.strptime(deadline, '%m/%d/%y')
    print (deadlineDate)
    daysLeft = deadlineDate - currentDate
    print(daysLeft)

    years = ((daysLeft.total_seconds())/(365.242*24*3600))
    yearsInt=int(years)

    months=(years-yearsInt)*12
    monthsInt=int(months)

    days=(months-monthsInt)*(365.242/12)
    daysInt=int(days)

    hours = (days-daysInt)*24
    hoursInt=int(hours)

    minutes = (hours-hoursInt)*60
    minutesInt=int(minutes)

    seconds = (minutes-minutesInt)*60
    secondsInt=int(seconds)

    print('You are {0:d} years, {1:d}  months, {2:d}  days, {3:d}  hours, {4:d} \
 minutes, {5:d} seconds old.'.format(yearsInt,monthsInt,daysInt,hoursInt,minutesInt,secondsInt))
# Funny link
def Never_Gonna_Give_You_Up():
    import webbrowser
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    import urllib.request
    get_url = urllib.request.urlopen('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    print("Response Status:"+ str(get_url.getcode()))
# Location of my saved code
def Saved_Code():
    import webbrowser
    webbrowser.open("https://docs.google.com/document/d/1kbdG_mxyPLB-DhCcLRXpHoWBdxUj1O1gDnH0BsludFI/edit")
    import urllib.request
    get_url = urllib.request.urlopen('https://docs.google.com/document/d/1kbdG_mxyPLB-DhCcLRXpHoWBdxUj1O1gDnH0BsludFI/edit')
    print("Response Status:"+ str(get_url.getcode()))
# The current date and time function 
def date_time():
    import time
    print(f"Todays date is {time.ctime()} ")
# Time conversion function 
def time_conversion():
    years = int(input("Please enter years: ")) * 365 * 24 * 60 * 60
    days = int(input("Please enter days: ")) * 3600 * 24
    hours = int(input("Please enter hours: ")) * 3600
    minutes = int(input("Please enter minutes: ")) * 60
    seconds = int(input("Please enter seconds: "))

    time = years + days + hours + minutes + seconds 

    print("The Total seconds:", time)
# Google Classroom function
def google_classroom():
    import webbrowser
    webbrowser.open("https://classroom.google.com/u/0/h")
    import urllib.request
    get_url = urllib.request.urlopen('https://classroom.google.com/u/0/h')
    print("Response Status:"+ str(get_url.getcode()))
# Youtube function 
def Youtube():
    import webbrowser
    webbrowser.open("https://www.youtube.com/")
    import urllib.request
    get_url = urllib.request.urlopen('https://www.youtube.com/')
    print("Response Status:"+ str(get_url.getcode()))
# Password and Username 
def main():
    while True:
        UserName = input ("Enter Username: ")
        PassWord = input ("Enter Password: ")

        if UserName == 'Alec' and PassWord == 'Green3827':
            time.sleep(1)
            print ("Login successful!")
            logged()

        else:
            print ("Password did not match!")
# Second menu code
def menu2():
     print("Page 2, \n 5. Launch Google Classroom \n 6. Time Conversion \n 7. How Old Am I? \n 8. Addition \n 9. Never Gonna Give You up \n 10. Previous Page")
# If password and username are correct
def logged():
    menu()
# The first menu code
def menu():
    print("Welcome, \n 1. Youtube \n 2. Todays Date \n 3. More Code \n 4. Saved code \n 5.Exit")
    option = input("Enter your choice: ")
    # All the options 
    if option == "1":
      Youtube()
      menu()
   
    if option == "3":
        menu2()
        option = input("Enter your choice: ")
        # Options for menu 2

        if option == "5":
            google_classroom()
            menu2()
        
        elif option == "6":
            time_conversion()
        elif option == "10":
            menu()
        elif option == "7":
            birthdate()
        elif option == "8":
            Add_Number()
        elif option == "9":  
           Never_Gonna_Give_You_Up()
          
    
    if option == "2":
        date_time()
        menu()

    if option == "4":
        Saved_Code()
        menu()

    if option == "5":
        print ("You have exited.")
        exit()
        
    # The try and except code     
    try:
        option = int(input)

    except:
        print("Wrong input")
        menu()









main()