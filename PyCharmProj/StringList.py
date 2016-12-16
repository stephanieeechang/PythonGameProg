'''
A function that takes a list of strings and prints them, one per line, in a rectangular frame.
'''
def printRectangle(stringList):
    vertical = len(stringList)
    horizontal = 0
    for i in range(len(stringList)):
        length = len(stringList[i])
        if length > horizontal:
            horizontal = len(stringList[i])
    print('*'*(horizontal+2))
    for v in range(vertical):
        print('*', end="")
        print(stringList[v], end="")
        for space in range(horizontal - len(stringList[v])):
            print(' ', end="")
        print('*')
    print('*'*(horizontal+2))


stringList = []
while str != '0':
    str = input('Enter a word (0 to end): ')
    if str != '0':
        stringList.append(str)

printRectangle(stringList)
