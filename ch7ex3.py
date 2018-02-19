fname = input('Enter the file name: ')
count = 0
try:
    fhand = open(fname)
except:
    if fname == 'na na boo boo':
        print("(Chuckle) I can't believe you actually typed that.")
    else:
        print('File name cannot be found:',fname)
    quit()
for line in fhand:
    if line.startswith('Subject:'):
        count = count +1
print('There were',count,'subject lines in',fname)