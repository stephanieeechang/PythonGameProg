'''
The program determines if the users input is within the range (within 10 of 100 or 200)
'''

#asks the user to input an interger, the value is stored in the variable n
n = input('Please enter an integer: ')

#if n is within the range of 10 to 100 or 200, withinRange would be True, if not, it would be False
withinRange = None

if n >= 10 and n<=100:
    withinRange = True
elif n == 200:
    withinRange = True
else:
    withinRange = False
