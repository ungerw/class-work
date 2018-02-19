fname = input('File name: ')
count = 0
try:
    fhand = open(fname)
except:
    print('File not found')
    quit()
else:
    for line in fhand:
        words = line.split()
        if len(words) == 0 : continue
        if words[0] != 'From' : continue
        print(words[2])