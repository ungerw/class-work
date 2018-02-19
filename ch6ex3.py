line = str(input('Enter a word: '))
text = str(input('Enter a letter in the word: '))
def count(line, letter):
    total = 0
    for letter in line:
        if letter == text:
            total = total + 1
    return total
print(count(line, text))