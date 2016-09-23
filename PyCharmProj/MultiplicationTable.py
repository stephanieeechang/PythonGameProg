'''
The program prints out the multiplication table of a given number
'''

number = input('Enter a number from 1 to 10: ')

print('Multiplication table of the number ' + str(number))

for i in range(1, 11):
    print(str(number) + ' x ' + str(i) + ' = ' + str(number*i))
