def computePay(hours, rate):
    # print('In computePay', hours, rate)

    hours = input('Enter Hours: ')
    rate = input('Enter Rate: ')
    # print('Do you work over time: ')
    # overTime = float(input())
    # requireHours = float(40.0)
    # wages = int(13)
    timeHalf = float(1.5)

    # Making Floating Variable

    fh = float(hours)
    fr = float(rate)

    if fh > 30:
        print('You work more than the required hours this week')
        reg = fh * fr
        # overTimeHour = fh - requireHours
        overTime = timeHalf * fr
        print('Do you work overtime: Y/N')
        que = input()
        if que == 'y':
            overTimeHour = int(input('overtime: '))
            overTimePay = overTime * overTimeHour
            xp = reg + overTimePay
            print('Pay:$', xp)
    else:
        print('Pay ', reg)


computePay(10, 11)

# print('Pay: ', xp)
