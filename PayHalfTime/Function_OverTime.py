def computePay(hours, rate):
    # print('In computePay', hours, rate)

    hours = input('Enter Hours: ')
    rate = input('Enter Rate: ')
    timeHalf = float(1.5)

    # Making Floating Variable

    fh = float(hours)
    fr = float(rate)

    reg = fh * fr    

    if fh > 40:
        print('You work more than the required hours this week')
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

