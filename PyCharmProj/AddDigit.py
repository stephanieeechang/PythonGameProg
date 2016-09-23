'''
The program add all digits of a number of the user's input until the result has only one digit
'''

number = str(input('Please enter a non-negative integer: '))
result = 10

while(result > 9):
    digit = len(number)
    for i in range(0, digit):
        if(i==0):
            result = 0
        result += int(number[i])
    number = str(result)
    print(number)

print('The sum is: ' + str(result))
