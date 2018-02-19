fname = input('Enter the file name: ')
fhand = open(fname)
total = 0.0
count = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence: '):
        line = float(line[20:])
        total = total + line
        count = count + 1
print('Average spam confidence: ',total/count)