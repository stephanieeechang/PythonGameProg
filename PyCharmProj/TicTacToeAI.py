'''
Use artificial inteligence on the Tic Tac Toe game
Computer  v.s. Human player
'''
import TicTacToeLibrary as tttLib

#dictionary to store the game
grid = {1:'o', 2:'x', 3:'o', 4:'o', 5:'x', 6:'x', 7:' ', 8:' ', 9:'x'}

turn = {'human':'x', 'machine':'o'}
#ask human player his/hers prefered symbol
symbol = raw_input('Who is starting? (H/M): ')
#x always starts
if (symbol.upper() == 'M'):
    turn = {'machine':'x', 'human':'o'}
    #data structure for this game
    data = {'grid':grid,
            'score':None,
            'children':None,
            'turn':turn['machine']}
elif (symbol.upper() == 'H'):
    #data structure for this game
    data = {'grid':grid,
            'score':None,
            'children':None,
            'turn':turn['human']}

availableCoor = []
cells = grid.values()
for i in cells:
    if(i == ' '):
        availableCoor.append(i)
numPossible = len(availableCoor)


def generateChildren(data):
    '''
    generates all possible moves in the game
    :param data: dictionary grid, turn, score, children
    :return children: a list of data
    '''
    children = []
    score = 0
    for key, value in data['grid'].items():
        if value == ' ':
            gridChild = grid.copy()
            gridChild[key] = data['turn']
            nextTurn = 'x' if data['turn']=='o' else 'o'
            print(' ')
            if(tttLib.winner(gridChild)):
                tttLib.displayGrid(gridChild)
                if(gridChild[key] == 'x'):
                    if(turn['human'] == 'x'):
                        score += 10
                    else:
                        score -= 10
                else:
                    if(turn['human'] == 'o'):
                        score += 10
                    else:
                        score -= 10
                gridStructChild = {'grid': gridChild,
                                   'score':score,
                                   'turn':nextTurn,
                                   'children':None}
                children.append(gridStructChild)
    print score
    return children

children = generateChildren(data)
