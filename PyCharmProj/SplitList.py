'''
Takes a string and creates a list with single words as elements.
'''
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


print splitString()
