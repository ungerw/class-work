fname = input('File name: ')
fhand = open(fname)
count = dict()
for line in fhand:
    words = line.split()
    if not len(words) == 0 and words[0] == 'From' :
        if words[2] not in count:
            count[words[2]] = 1
        else:
            count[words[2]] += 1
print(count)