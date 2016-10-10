'''
A function that returns the elements on odd positions in a list.
'''

def odd(nList):
    oddList = []
    length = len(nList)
    for i in range(1, length, 2):
        oddList.append(nList[i])
    return oddList

numList = []
num = 1
while(num != 0):
    num = input('Enter numbers (0 to end): ')
    if num != 0:
        numList.append(num)

print odd(numList)
