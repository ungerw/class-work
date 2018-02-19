try:
    score = float(input('Enter Score = '))
    if score < 0.6:
        print('F')
    elif score <= 0.7:
        print('D')
    elif score <= 0.8:
        print('C')
    elif score <= 0.9:
        print('B')
    elif score <= 1.0:
        print('A')
    elif score > 1.0:
        print('Invalid answer')
except:
    print('Please enter score as decimal score')