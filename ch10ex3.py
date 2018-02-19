fname = input('File name: ')
count = dict()
try:
    fhand = open(fname)
except:
    print('File not found')
    quit()
else:
    for line in fhand:
        line = line.lower()
        for v in line:
            if v not in 'abcdefghijklmnopqrstuvwxyz' : continue
            if v not in count:
                count[v] = 1
            else:
                count[v] += 1
lst = list()
for key, val in count.items():
    lst.append((val, key))
lst.sort(reverse = True)
for key, val in lst:
    print(key, val)