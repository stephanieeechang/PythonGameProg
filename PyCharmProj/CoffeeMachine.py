'''
PAS coffee maker
'''
import time
from threading import Thread

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
answer = None

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
        start = False
        continue

    sugar = input('Select the portions of sugar (0~5): ')

    price = product + sugar
    print('The price of your beverage is ' + str(price) + ' NTD.')

    def check():
        time.sleep(10)
        if(answer == 'START'):
            start == True
            return
        elif(answer == 'CANCEL'):
            cancel == True
            return
        else:
            start == False
            print('\nRestarting...')
            return 0

    Thread(target = check).start()
    answer = raw_input('START or CANCEL? You have 10 seconds to input...')
    if(answer == 'START'):
        break

for t in range(productTime, 0, -1):
    print(str(t) + 'seconds left till your beverage ready...')
    time.sleep(1)

print('Your beverage is ready!')
