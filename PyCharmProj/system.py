'''
Calculate the average of two numbers

The numbers are passed as arguments to the script
'''


import sys
print('The arguments passed were: ')
print(sys.argv)

a = float(sys.argv[1]) #first argument
b = float(sys.argv[2]) #second argument

print('The average is ')
print((a+b)/2)
