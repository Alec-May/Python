def Add_Number():
    number1 = input("Enter the first number: ")
    number2 = input("Enter the last number: ")
    Sum = int(number1) + int(number2)
    print(Sum)

def Never_Gonna_Give_You_Up():
    import webbrowser
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    import urllib.request
    get_url = urllib.request.urlopen('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    print("Response Status:"+ str(get_url.getcode()))