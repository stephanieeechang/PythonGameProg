'''
The program converts a binary to a decimal number.
'''
import math

dec = 0
bin = raw_input('Enter only 1s and 0s (10111): ')
digit = len(bin)

while(sum(map(int,str(bin))) > digit):
    bin = raw_input('Enter only 1s and 0s (10111): ')
    digit = len(bin)

for c in range(1, digit+1):
    dec += int(bin[c-1]) * math.pow(2, digit-c)
print('Decimal number is ' + str(dec))
