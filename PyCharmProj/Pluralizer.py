'''
user inputs a number and an object (in singular form),
the program translates the number into word and prints it with the plural form of the object
'''

numDict = {1:'one', 2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten'}

object = raw_input('Enter an object: ')
num = input('Enter the quantity of the object(1~10): ')

if num > 1 and num < 10:
    if object[-1:] == 'a' or object[-1:] == 'i' or object[-1:] == 'o' or object[-1:] == 'u' or object[-1:] == 's'\
            or object[-1:] == 'x' or object[-1:] == 'z' or object[-2:] == 'ch' or object[-2:] == 'sh':
        plural = object + 'es'
    else:
        plural = object + 's'
    print numDict[num] + ' ' + plural
elif num < 1 or num > 10:
    print 'Invalid quantity!'
else:
    plural = object
    print numDict[num] + ' ' + plural
