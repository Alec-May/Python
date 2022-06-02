menu_options ={
    1: 'Hello World',
    2: 'Date/Time',
    3: 'empty',
    4: 'Hello',
    5: 'Launch Youtube',
    6: 'More Code',
    7: 'Exit',
}
# Creating the menu
def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )
# The hello option
def hello():
    print('Hello World')
# The date and time function
def date_time():
    import time
    print(f"Todays date is {time.ctime()} ")
# Undefined Option 2
def empty():
    print("Empty")
# The greeting function  
def Name():
    name = input("Your name: ")
    import time
    # Using f-string to connect the variables with the string
    print(f"Hello! {name} thank you for being here. Todays date is {time.ctime()}")
Name()
def Youtube():
    import webbrowser
    webbrowser.open("https://www.youtube.com/")
    import urllib.request
    get_url = urllib.request.urlopen('https://www.youtube.com/')
    print("Response Status:"+ str(get_url.getcode()))
def More_Code():
    print("**********More Code**********")
    print("1: Launch Google Classroom")
    print("2: Placeholder")
    print("3: Placeholder")

# The except, if, else if and else options
if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        if option == 1:
            hello()
        elif option == 2:
            date_time()
        elif option == 3:
            empty()
        elif option == 7:
            print('You have exited')
            exit()
        elif option == 4:
            Name()
        elif option == 5:
            Youtube()
        elif option == 6:
            More_Code()
        else:
            print ('Invalid option. Please enter a number between 1 and 6')
           
           
 
 

