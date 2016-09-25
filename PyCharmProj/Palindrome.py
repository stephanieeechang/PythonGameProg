'''
The program determines if a string passed as an argument in the terminal is a palindrome.
'''

inputString = raw_input('Enter a string: ')
characters = len(inputString)
same = True

for i in range(0, characters, 1):
    if(inputString[i] == inputString[characters-(i+1)]):
        same = True
    else:
        same = False

if(same):
    print(inputString + ' is a palindrome.')
else:
    print(inputString + ' is not a palindrome.')
