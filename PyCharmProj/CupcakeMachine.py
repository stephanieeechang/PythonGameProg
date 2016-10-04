'''
The program runs a cupcake machine
'''
import time
from threading import Thread
import signal

chocolate = 50
vanilla = 30
redVelvet = 45
cherryP = 5
frostingP = 10
cTime = 10
vTime = 6
rTime = 8
cherry = False
frosting = False
productTime = 0
productPrice = 0
start = False
TIMEOUT = 10

def menu():
    #flavor
    print('Choose a product: ')
    flavor = input('1-Red Velvet     2-Chocolate     3-Vanilla\n')

    #cherry
    cherryYN = raw_input('Cherry? (Y/N): ')
    if(cherryYN == 'Y'):
        cherry = True
    elif(cherryYN == 'N'):
        cherry = False
    else:
        print('Invalid input!')
        restart()

    #frosting
    frostingYN = raw_input('Frosting? (Y/N): ')
    if(frostingYN == 'Y'):
        frosting = True
    elif(frostingYN == 'N'):
        frosting = False
    else:
        print('Invalid input!')
        restart()

    #price
    if(flavor == 1):
        price = redVelvet
        time = rTime
    elif(flavor == 2):
        price = chocolate
        time = cTime
    elif(flavor == 3):
        price = vanilla
        time = vTime
    else:
        print('Invalid input!')
        restart()
    if(cherry):
        price += cherryP
    if(frosting):
        price += frostingP
    return price, time

def check():
    print('START or CANCEL? You have 10 seconds to input...')
    signal.alarm(TIMEOUT)
    answer = raw_input()
    signal.alarm(0)
    if answer == 'START':
        start = True
        countdown()
        print('Your cupcake is ready!')
        return start
    else:
        print('Restarting...')
        restart()

def countdown():
    for t in range(productTime, 0, -1):
        print(str(t) + 'seconds left till your cupcake ready...')
        time.sleep(1)

def restart():
    productPrice, productTime = menu()
    print('The price of your cupcake is ' + str(productPrice) + ' NTD.')
    Thread(target=check).start()

restart()
