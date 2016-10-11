'''
A function that counts how many times a word appears in a text.
'''
def count():
    list1 = splitString()
    list2 = []
    occurrence = []

    for word in list1:
        if word in list2:
            occurrence[list2.index(word)] += 1
        else:
            list2.append(word)
            occurrence.append(1)

    for i in range(len(list2)):
        print('The occurrence of ' + list2[i] + ' is ' + str(occurrence[i]) + ' times.')

def splitString():
    sentence = raw_input('Enter a string: ')
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
    return splitList

count()
