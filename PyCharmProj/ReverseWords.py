'''
The program accept a word from the user and reverse it using for loops
'''

word = input('Please enter a word for reversing: ')
letters = len(word)

for i in range(letters-1, -1, -1):
    print(word[i], end="")

print('')
