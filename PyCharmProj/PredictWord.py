'''
predicts the next word
'''

import MyLibrary as ml
import random


def randomWord(words, density):
    '''
    The function picks out a random word from the words list
    :param density: list of next possible words
    :param words: list of probability density
    :return: a random word from the list
    '''
    n = random.random()
    index = 0
    while n > density[index]:
        index += 1
    return words[index]


theWord = raw_input('Enter the word: ')
numOfWords = input('How many words would you like to predict? ')

sampleText = 'PredictWordText.txt'
txtList = ml.readTxt(sampleText)

predictedText = ''

for i in range(numOfWords):
    nextWord, freq = ml.nextWord(theWord, txtList)
    #print (nextWord, freq)

    probabilityList = ml.calcProbability(freq)
    #print probabilityList

    prob = ml.calcProbability(probabilityList)
    #print prob

    word = randomWord(nextWord, prob)
    predictedText += (' ' + word)

print predictedText
