'''
The program counts the number of times of getting a 6 on a dice out of 1000 rolls,
while it randomly rolls the dice (generates random number ranging from 1~6)
Also calculates the probability of getting a 6 in a dice roll.
'''
import random
n = 0
dice6 = 0

while n < 1000:
    dice = random.randint(1, 6)
    if dice == 6:
        dice6 += 1
    n += 1

probability = dice6/ 1000 * 100
print('The occurrences of getting a 6 on a dice is ' + str(dice6) + ' times out of 1000 rolls.')
print('The probability is ' + str(probability) + '%')
