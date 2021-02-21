def computePay(hours, rate):
    print('In computePay', hours, rate)

    hours = input('Enter Hours: ')
    rate = input('Enter Rate: ')
    wages = int(13)
    timeHalf = float(1.5)

    # Making Floating Variable

    fh = float(hours)
    fr = float(rate)

    if fh > 40:
        print('You work more than the require hours of work')
        reg = fh * wages
        overTimeHour = fh - fh
        overTime = timeHalf * wages
        overTimePay = overTime * overTimeHour
        xp = reg + overTimePay
    else:
        pay = hours * rate

    print(pay)  # pay


computePay(fh, fr)
