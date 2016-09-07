'''
The program extracts the digit of a number.
User enters a natural number.
'''
number = input('Enter a natural number: ')
n = 0
mod = 1
while mod != 0:
    mod, res = divmod(int(number), 10)
    number = mod
    n += 1
    print('Digit #' + str(n) + ' = ' + str(res))
