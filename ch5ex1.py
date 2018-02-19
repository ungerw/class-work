count = 0
total = 0
while True:
    line = input('Enter a number: ')
    if line == 'done':
        break
    try:
        num = float(line)
    except:
        print('Invalid input')
        continue
    count = count + 1
    total = total + num
print(total,count,total/count)