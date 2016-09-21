'''
MasterMind is a number game.
The program randomly generates a 5-digit secret number (the digits do not repeat).
The object of the game is to guess that secret number.
After each guess, the program will tell the user the number of digits in the guess number that match or occur in the secret number (White hits),
and how many of the digits are in the correct position (Black hits) in the secret number.
'''
import random
import sys

#set the number of digits in the game
numDigits = 5

# create the secret number as a concatenation of string digits
secretNum = ""
for i in range(numDigits+1):
    if(i == 0):
        digit0 = str(random.randint(0, 9))
        secretNum = digit0

    elif(i==1):
        digit1 = str(random.randint(0, 9))
        if(digit1 == digit0):
            digit1 = str(random.randint(0, 9))
            i -= 1
        else:
            secretNum += digit1

    elif(i==2):
        digit2 = str(random.randint(0, 9))
        if (digit2 == digit0 or digit2 == digit1):
            digit2 = str(random.randint(0, 9))
            i -= 1
        else:
            secretNum += digit2

    elif(i==3):
        digit3 = str(random.randint(0, 9))
        if(digit3 == digit0 or digit3 == digit1 or digit3 == digit2):
            digit3 = str(random.randint(0, 9))
            i -= 1
        else:
            secretNum += digit3

    elif(i==4):
        digit4 = str(random.randint(0, 9))
        if(digit4 == digit0 or digit4 == digit1 or digit4 == digit2 or digit4 == digit3):
            digit3 = str(random.randint(0, 9))
            i -= 1
        else:
            secretNum += digit4

#print(secretNum)

#initialize the user's input
userNum = 0

#tries counter for user
iterations = 1
#initialize black hits to 0
blackHits = 0

while blackHits < 5:
    userNum = int(input('Please enter a 5 digit number (10000~99999): '))
    while userNum < 10000 or userNum > 99999:
        userNum = int(input('Please enter a 5 digit number (10000~99999): '))
    blackHits = 0
    whiteHits = 0
    cntDigit = 0
    iterations += 1

    #check every digit in the user's input
    for d in str(userNum):
        #check if digit exists in the secret number
        if (d in secretNum):
            #position of digit in the secret number
            posDigit = secretNum.index(d)
            #check if position matches
            if(posDigit == cntDigit):
                blackHits += 1
            else:
                whiteHits += 1
        #check next digit in the user's input
        cntDigit += 1
    #print hits
    print('Black hits: ' + str(blackHits))
    print('White hits: ' + str(whiteHits))

#show tries after the user won the game
print('You win! It took you ' + str(iterations) + ' tries.')
