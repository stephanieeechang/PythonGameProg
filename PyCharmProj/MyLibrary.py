'''
Stores all functions!!!!!
'''
import random


def randomNum(max, min):
    number = random.randint(min, max)
    return number


def splitString(x):
    return x.split()


def countWord():
    '''
    counts the occurrence of a word
    :return: the list of words, list of occurrence to each corresponding word
    '''
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

    return list2, occurrence


def readTxt(nameFile):
    '''
    This function reads a txt file
    :param nameFile: address to the .txt file
    :return: a list
    '''
    f = open(nameFile, 'r')
    outputList = f.read().lower()
    f.close()
    return splitString(outputList)


def calcProbability(frequency):
    '''
    calculate the probability of a word being the next word
    :param frequency: a list of the number of occurrence of a word in the text
    :return: a list of the words' density
    '''
    denominator = sum(frequency)
    #list comprehension
    probList = [1.0*i/denominator for i in frequency]
    density  = []
    total = 0
    for p in probList:
        total += p
        density.append(total)
    return density


def nextWord(word, text):
    '''
    Find the next word of the given word
    :param currentWord: given word
    :param text: the sample text
    :return: a list with the following words, frequency
    '''
    nextWordList = []
    frequency = []
    for index, element in enumerate(text):
        if element == word:
            next = text[index+1]
            #print('Next word is %r'% (next))
            if next in nextWordList:
                frequency[nextWordList.index(next)]+=1
            else:
                nextWordList.append(next)
                frequency.append(1)
    return nextWordList, frequency
