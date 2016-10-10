'''
A function that combines two lists by alternately taking elements.
'''
def combine(l1, l2, length):
    cList = []
    iter = length*2
    a = 0
    b = 0
    for i in range(iter):
        if i % 2 == 0:
            cList.append(l1[a])
            a += 1
        else:
            cList.append(l2[b])
            b += 1
    return cList

length1 = 0
length2 = 1
while(length1 != length2):
    list1 = []
    x = 1
    while(x != 0):
        x = input('Enter numbers for the first list (0 to end): ')
        if x != 0:
            list1.append(x)
    length1 = len(list1)

    list2 = []
    y = 1
    while(y != 0):
        y = input('Enter numbers for the second list (0 to end): ')
        if y != 0:
            list2.append(y)
    length2 = len(list2)

print combine(list1, list2, length1)
