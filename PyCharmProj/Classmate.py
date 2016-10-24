'''
The program randomly generates one of the classmates' name
'''
import random

def randomCmate(inputList = ['Alex', 'Cici', 'Daniel', 'Darren', 'Sabrina', 'Stephanie']):
    '''
    Selects a classmate at random
    :param inputList: a list of the classmates' names
    (with default value of all classmates' names)
    :return: a name
    '''
    edit = raw_input('Would you like to edit the list? (y/n) ')
    if edit == 'y':
        inputList = []
        numStudents = input('How many students are in the class? ')
        for i in range(numStudents):
            inputName = raw_input('Enter a name: ')
            inputList.append(inputName)
    numStudents = len(inputList)
    randomNum = random.randint(0, numStudents-1)
    name = inputList[randomNum]
    return name

name = randomCmate(inputList = ['Alex', 'Cici', 'Daniel', 'Darren', 'Sabrina', 'Stephanie'])
print name
