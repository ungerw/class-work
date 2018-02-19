try:
    hours = float(input('Enter Hours: '))
    rate = float(input('Enter Rate: '))
    if hours <= 40:
        computepay = hours * rate
        print(computepay)
    elif hours > 40:
        computepay = (40 * rate) + ((hours - 40) * (rate * 1.5))
        print(computepay)
except:
    print('Error, please enter a numeric input')