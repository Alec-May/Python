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

birthdate()


    
