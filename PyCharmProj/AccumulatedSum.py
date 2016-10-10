'''
Input a list, output the accumulated sum of a list.
'''

numList = []
num = 1
while(num != 0):
    num = input('Enter numbers (0 to end): ')
    if num != 0:
        numList.append(num)

sum = 0
outputList = []
for i in numList:
    sum += i
    outputList.append(sum)

print outputList
