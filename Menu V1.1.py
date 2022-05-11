# Opens Youtube
def Youtube():
    import webbrowser
    webbrowser.open("https://www.youtube.com/")
    import urllib.request
    get_url = urllib.request.urlopen('https://www.youtube.com/')
    print("Response Status:"+ str(get_url.getcode()))
# Time Conversion challenge 
def time_conversion():
    years = int(input("Please enter years: ")) * 365 * 24 * 60 * 60
    days = int(input("Please enter days: ")) * 3600 * 24
    hours = int(input("Please enter hours: ")) * 3600
    minutes = int(input("Please enter minutes: ")) * 60
    seconds = int(input("Please enter seconds: "))

    time = years + days + hours + minutes + seconds 

    print("The Total seconds:", time)
# Brings up my saved code document 
def Saved_Code():
    import webbrowser
    webbrowser.open("REDACTED")
    import urllib.request
    get_url = urllib.request.urlopen('REDACTED')
    print("Response Status:"+ str(get_url.getcode()))
# Placeholder
def placeholder():
    print("Placeholder")
# Date and time challenge 
def date_time():
    import time
    print(f"Todays date is {time.ctime()} ")
# Code for menu 2
def menu2():
     print("Page 2, \n 5. Launch Google Classroom \n 6. Time Conversion \n 7. Previous Page")
# Opens google classroom
def google_classroom():
    import webbrowser
    webbrowser.open("REDACTED")
    import urllib.request
    get_url = urllib.request.urlopen('REDACTED')
    print("Response Status:"+ str(get_url.getcode()))
# Code for original menu    
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
        elif option == "7":
            menu()
    
    if option == "2":
        date_time()
        menu()

    if option == "4":
        Saved_Code()
        menu()

    if option == "5":
        print ("You have exited.")
        exit() 
    # The try and execpt code     
    try:
        option = int(input)

    except:
        print("Wrong input")
        menu()

# Calls the function 
menu()

