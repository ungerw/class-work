answer = []
while True:
    line = input('Enter a number: ')
    if line == 'done':
        break
    try:
        num = float(line)
    except:
        print('Invalid input')
        continue
    n = answer.append(num)
biggest = max(answer)
smallest = min(answer)
print('Maximum:',biggest)
print('Minimum:',smallest)