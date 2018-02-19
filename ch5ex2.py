biggest = None
smallest = None
while True:
    line = input('Enter a number: ')
    if line == 'done':
        break
    try:
        num = float(line)
    except:
        print('Invalid input')
        continue
    if smallest is None or num < smallest:
        smallest = num
    if biggest is None or num > biggest:
        biggest = num
print('Max:',biggest,'Min:',smallest)