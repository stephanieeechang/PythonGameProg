'''
The program asks the user if monkeys a and b are smiling, then determines whether the user is in trouble.
'''
#import sys

#asks the user if the monkeys are smiling
smiling = input('Are monkeys a and b smiling? (a, b, both, neither): ')

#print('Are monkeys a and b smiling? (a, b, both, neither): ')
#print(sys.argv)

#stores the user's input to the variable smiling
#smiling = str(sys.argv[0])

a_smile = None
b_smile = None

#stores the answers into booleans a_smile and b_smile
if smiling == 'a':
    a_smile = True
    b_smile = False
elif smiling == 'b':
    a_smile = False
    b_smile = True
elif smiling == 'both':
    a_smile = True
    b_smile = True
elif smiling == 'neither':
    a_smile = False
    b_smile = False
else:
    print('Please input a valid answer!')

#prints out the result
if a_smile == True and b_smile == False:
    print('We are fine.')
elif a_smile == False and b_smile == True:
    print('We are fine.')
elif a_smile == True and b_smile == True:
    print('We are in trouble.')
elif a_smile == False and b_smile == False:
    print('We are in trouble.')
