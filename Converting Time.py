def time_conversion():
    days = int(input("Please enter days: ")) * 3600 * 24
    hours = int(input("Please enter hours: ")) * 3600
    minutes = int(input("Please enter minutes: ")) * 60
    seconds = int(input("Please enter seconds: "))

    time = days + hours + minutes + seconds 

    print("The Total seconds:", time)

time_conversion()