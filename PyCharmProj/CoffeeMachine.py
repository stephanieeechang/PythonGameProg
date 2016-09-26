'''
PAS coffee maker
'''
import sys
import time

latteS = 20
latteL = 30
latteTime = 6
americanoS = 30
americanoL = 50
americanoTime = 4
expressoS = 25
expressoL = 40
expressoTime = 5
start = False
cancel = False
price = 0

while(start == False or cancel == True):
    print('Choose a product: ')
    beverage = input('1-Latte      2-Americano     3-Expresso\n')
    print('Choose size: ')
    size = input('1-Large     2-Small\n')

    if(beverage == 1 and size == 1):
        product = latteL
        productTime = latteTime
    elif(beverage == 1 and size == 2):
        product = latteS
        productTime = latteTime
    elif(beverage == 2 and size == 1):
        product = americanoL
        productTime = americanoTime
    elif(beverage == 2 and size == 2):
        product = americanoS
        productTime = americanoTime
    elif(beverage == 3 and size == 1):
        product = expressoL
        productTime = expressoTime
    elif(beverage == 3 and size == 2):
        product = expressoS
        productTime = expressoTime
    else:
        print('The product does not exist!')
        sys.exit()

    sugar = input('Select the portions of sugar (0~5): ')

    price = product + sugar
    print('The price of your beverage is ' + str(price) + ' NTD.')

    #sec10 = 10
    #while(sec10 > 0):
    enterC = raw_input('Input "c" to cancel. Press [ENTER] to skip to the next step.')
    if(enterC == 'c'):
        cancel == True
    enterS = raw_input('Input "s" to start.')
    if(enterS == 's'):
        start = True
        #sec10 -= 1
        #time.sleep(1)

    for t in range(productTime, -1, -1):
        print(str(t) + 'seconds left till your beverage ready...')
        time.sleep(1)

print('Your beverage is ready!')
