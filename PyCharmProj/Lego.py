'''
The program categorises Lego bricks and beams by using the distance formula
(the weight and length of Legos are given in the Lego.txt file, then import file into the program),
and plots a scatter plot for a clearer vision in the distribution of the 2000 Legos.

Source: http://stackoverflow.com/questions/15192847/saving-arrays-as-columns-with-np-savetxt
'''
# library for scientific computations
import numpy as np
#library for graphs
import matplotlib.pyplot as plt
import math

# read Legos.txt file
legos = np.loadtxt('Legos.txt',delimiter=',')
beamCoor = np.loadtxt('BeamsCoordinates.txt',delimiter=',')
brickCoor = np.loadtxt('BricksCoordinates.txt',delimiter=',')

numBeams = 0
numBricks = 0
repBeamL = 3
repBeamW = 5
repBrickL = 7
repBrickW = 4

# show the dimensions of legos (# of rows, # columns)
np.shape(legos)


def printPoints():
    for x, y in legos:
        print(x, y)


def calc(distanceBrick, distanceBeam, bricksCalc, beamsCalc):
    if(distanceBeam > distanceBrick):
        bricksCalc += 1
        isBrick = True
    else:
        beamsCalc += 1
        isBrick = False
    return bricksCalc, beamsCalc, isBrick


def distance():
    bricks = 0
    beams = 0
    brickListX = []
    brickListY = []
    beamListX = []
    beamListY = []
    for x, y in legos:
        distanceBeam = math.sqrt((repBeamL - x)**2 + (repBeamW - y)**2)
        distanceBrick = math.sqrt((repBrickL - x)**2 + (repBrickW - y)**2)
        bricks, beams, isBrick = calc(distanceBrick, distanceBeam, bricks, beams)
        if(isBrick):
            brickListX.append(x)
            brickListY.append(y)
        else:
            beamListX.append(x)
            beamListY.append(y)
    np.savetxt('BricksCoordinates.txt', np.c_[brickListX, brickListY], delimiter=',')
    np.savetxt('BeamsCoordinates.txt', np.c_[beamListX, beamListY], delimiter=',')
    print('Number of bricks: ' + str(bricks))
    print('Number of beams: '+ str(beams))


def plot():
    # print each pair of points in a scatter plot
    for x, y in beamCoor:
        plt.scatter(x,y,color='gray')
        plt.show()
    for a, b in brickCoor:
        plt.scatter(a,b,color='blue')
        plt.show()

printPoints()
distance()
plot()
