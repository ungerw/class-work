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
            d1, d2, d3 = words[5].split(':')
            if d1 not in count:
                count[d1] = 1
            else:
                count[d1] += 1
lst = list()
for key, val in count.items():
    lst.append((val, key))
lst.sort()
for key, val in lst:
    print(key, val)