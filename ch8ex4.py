fname = input('File name: ')
answer = []
try:
    fhand = open(fname)
except:
    print('File not found')
    quit()
else:
    for line in fhand:
        list = line.split()
        for word in list:
            if word in answer: continue
            answer.append(word)
answer.sort()
print(answer)