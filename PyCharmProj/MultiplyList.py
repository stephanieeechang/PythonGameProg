'''
Multiply all numbers in a list, skip non-numeric values.
'''

def multiply(fList):
    product = 1
    for i in fList:
        product *= i
    return product


def nonNumeric(num):
    if type(num) is int:
        return True
    elif type(num) is long:
        return True
    elif type(num) is float:
        return True


numList = []
num = 1
while(num != 0):
    num = input('Enter numbers for multiplication (0 to end): ')
    if num != 0:
        numList.append(num)

filterList = filter(nonNumeric, numList)
print(multiply(filterList))
