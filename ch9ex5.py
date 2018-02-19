fname = input('File name: ')
count = dict()
try:
    fhand = open(fname)
except:
    print('File not found')
    quit()
else:
    for line in fhand:
        words = line.split()
        if not len(words) == 0 and words[0] == 'From' :
            start = words[1].find('@')
            domain = words[1][start+1:]
            if domain not in count:
                count[domain] = 1
            else:
                count[domain] += 1
print(count)