'''
Create list from 0 to 10
'''

a = 0
myList = []
while a <= 10:
    myList.append(a)
    a+=1

print myList


'''
Concise way to create a list
'''
list2 = [x**2 for x in range(11)]
print list2

'''
Combines the elements of two lists if !=
'''
A = [1,2,3]
B = [4,5,6]
C = []

for a in A:
    for b in B:
        if a != b:
            C.append((a,b))
print C

C = [(a,b) for a in A, b in B if a!=b ]

'''
Count occurrence
'''
sentence = 'the quick brown fox jumps over the lazy dog'
splitList = []
word = ''
for letter in sentence:
    if letter == ' ':
        splitList.append(word)
        word = ''
    else:
        word += letter
if word != '':
    splitList.append(word)

list1 = splitList
list2 = [1 for word in list1 if word == 'the']

occurrence = 0
for i in list2:
    occurrence += i

print('The occurrence of the is ' + str(occurrence) + ' times.')
