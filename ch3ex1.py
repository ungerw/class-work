hours = float(input('Hours Worked: '))
rate = float(input('Rate of Pay: '))
if hours <= 40:
    pay = hours * rate
    print(pay)
elif hours > 40:
    pay = (40 * rate) + ((hours - 40) * (rate * 1.5))
    print(pay)