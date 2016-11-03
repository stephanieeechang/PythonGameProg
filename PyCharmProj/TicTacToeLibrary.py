'''
Library foe storing all functions used in the TicTacToe program
'''

def displayGrid(sym):
    '''
    prints out grid and values of cell
    :param sym: x, o, or blank (value)
    :return: none
    '''
    print('       |       |       ')
    print('   %s   |   %s   |   %s   ' %(sym[1], sym[2], sym[3]))
    print('       |       |       ')
    print('-----------------------')
    print('       |       |       ')
    print('   %s   |   %s   |   %s   ' %(sym[4], sym[5], sym[6]))
    print('       |       |       ')
    print('-----------------------')
    print('       |       |       ')
    print('   %s   |   %s   |   %s   ' %(sym[7], sym[8], sym[9]))
    print('       |       |       ')


def winner(ox):
    '''
    determines the winner of the game
    :param ox: the values of the dictionary (x or o or blank)
    :return: if there is a line (bingo)
    '''
    same = None
    win = ''
    for i in range(0, 3):
        if(ox[1+3*i]==ox[2+3*i] and ox[1+3*i]==ox[3+3*i] and ox[1+3*i]!=' ' and ox[2+3*i]!=' ' and ox[3+3*i]!=' '):
            same = True
            return same
    for i in range(1, 4):
        if(ox[i]==ox[i+3] and ox[i]==ox[i+6] and ox[i]!=' ' and ox[i+3]!=' ' and ox[i+6]!=' '):
            same = True
            return same
    if(ox[1]==ox[5] and ox[1]==ox[9] and ox[1]!=' ' and ox[5]!=' ' and ox[9]!=' '):
        same = True
    elif(ox[3]==ox[5] and ox[3]==ox[7] and ox[3]!=' ' and ox[5]!=' ' and ox[7]!=' '):
        same = True
    else:
        same = False
    return same


def inputOX(userDict):
    '''
    players choose which position he/she wants to put a symbol (o or x) at,
    two players have alternating turns.
    displays the grid after each round.
    determines whether if there is a winner.
    :param userDict: the dictionary storing the symbols
    :return: none
    '''
    count = 0
    symbol = ''
    chosenCoor = []
    while(count < 9):
        if(count%2 == 0):
            print("Player o's turn")
            symbol = 'o'
        else:
            print("Player x's turn")
            symbol = 'x'

        userKey = input('Pick a coordinate(1~9): ')
        #check if the coordinate is chosen
        if(userKey in chosenCoor):
            print('Coornidate already chosen! Pick another one.')
            continue
        userDict[userKey] = symbol
        chosenCoor.append(userKey)

        count += 1
        displayGrid(userDict)
        bingo = winner(userDict)
        if(bingo == True):
            if(symbol == 'x'):
                print('Player x wins!')
                exit()
            else:
                print('Player o wins!')
                exit()
    print('Tie.')

'''
def artificialIntelligence(currentDict):
    availableCoor = []
    if(winner(currentDict)==True):
        return currentDict
'''
