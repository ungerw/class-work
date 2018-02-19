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
            if words[1] not in count:
                count[words[1]] = 1
            else:
                count[words[1]] += 1
lst = list()
for key, val in count.items():
    lst.append((val, key))
lst.sort(reverse=True)
for key, val in lst[:1]:
    print(key, val)