str = 'X-DSPAM-Confidence:0.8475'
mark = str.find(':')
number = float(str[mark+1:])
print(number)