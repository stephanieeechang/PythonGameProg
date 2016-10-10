'''
A function for printing menus in the terminal.
'''
import sys


def menu(menuList):
    numOptions = len(menuList)
    print('The options are:')
    for i in range(numOptions):
        print('\t' + str(i+1) + '. ' + menuList[i])
    preference = raw_input('What is your preference (1-' + str(numOptions) + ')? Press X to exit: ')
    return preference

menuList = ['Meat', 'Fish', 'Chicken']
choice = menu(menuList)
if choice == 'X':
    sys.exit()
else:
    choice = int(choice)
    print('You chose: ' + menuList[choice-1])
