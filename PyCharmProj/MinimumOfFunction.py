'''
The program finds the minimum of a function of the user's choice
'''
import math
import random

functionA = float(input('Enter the coefficient of the variable to the second power (ax^2, enter a): '))
functionB = float(input('Enter the coefficient of the variable to the first power (bx, enter b): '))
functionC = float(input('Enter the constant: '))
variableX = random.randint(-100, 100)

#f(x), when x = random int (between -100 and 100)
functionOutput = functionA * math.pow(variableX, 2) + functionB * variableX + functionC

#set slope to 1
slope = 1
#increment x
variableX += slope

#get f(x) after x is incremented by the slope
newFunctionOutput = functionA * math.pow(variableX, 2) + functionB * variableX + functionC

#change slope to be sure that the point is approaching the minimum in the correct direction
if newFunctionOutput > functionOutput:
    slope = -1
else:
    slope = 1

#get minimum
while abs(newFunctionOutput - functionOutput) > 0.1:
    functionOutput = functionA * math.pow(variableX, 2) + functionB * variableX + functionC
    newVariableX = variableX + slope
    newFunctionOutput = functionA * math.pow(newVariableX, 2) + functionB * variableX + functionC
    minimum = newFunctionOutput
    variableX = newVariableX

print('The minimum of the function is: ' + str(variableX))
