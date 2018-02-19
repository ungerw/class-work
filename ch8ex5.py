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
        if not len(words) == 0 and words[0] == 'From' :
            print(words[1])
            count = count + 1
print('There were',count,'lines in the file with From as the first word.')