'''
The program prints the first nth prime numbers, where the user enters the number n.
(utilizing for loop)
'''

n = int(input('Enter an integer: '))
times = 0
num = 2

while (times < n):
    num += 1
    noPrime = False
    if (times == 0):
        print ('2')
        times += 1
    for i in range(2, num):
        if ((num % i) == 0):
            noPrime = True
            break
    if (noPrime == False):
        print (num)
        times += 1
