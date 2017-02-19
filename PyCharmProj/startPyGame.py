import pygame as pg
import sys
from pygame.locals import *
import random


def drawGrid(win, winSize, cellSize, color):
    """
    Draws the grid for the game
    :param win: identifier of the window
    :param winSize: winSize (width,height)
    :param cellSize: width/length of each block
    :param color: RGB values of the line
    """

    for x in range(0, winSize[0], cellSize):  # draw vertical lines
        pg.draw.line(win, color, (x, 0), (x, winSize[1]))

    for y in range(0, winSize[1], cellSize):  # draw horizontal lines
        pg.draw.line(win, color, (winSize[0], y), (0, y))


def drawWorm(win, wormCoor, cellSize, wormColor):
    """
    Draws the worm for the game
    :param win: identifier of the window
    :param wormCoor: list with multiple dictionaries of x/y coordinates
    :param cellSize: width/length of each block
    :param wormColor: RGB values of worm
    """
    (a, b, c) = wormColor
    for i, c in enumerate(wormCoor):

        x = c['x'] * cellSize
        y = c['y'] * cellSize

        wormSegmentRect = pg.Rect(x, y, cellSize, cellSize)
        color = wormColor

        # Makes the head different color for identification
        if i == 0:
            color = (155, 0, 0)
        elif i == 1:
            color = (190, 0, 00)

        pg.draw.rect(win, color, wormSegmentRect)  # Draws out the worm


def drawApple(win, appleSize, appleColor, x, y):
    """
    Draws the apple for the game
    :param win: identifier of the window
    :param appleSize: width/length of each block
    :param appleColor: RGB values of apple
    :param x: x coordinates of the apple
    :param y: y coordinates of the apple
    """
    appleRect = pg.Rect(x, y, appleSize, appleSize)
    pg.draw.rect(win, appleColor, appleRect)  # Draws the apple


def randCoord():
    """
    Generates random x/y coordinates for apple reference
    :return: x/y coordinates
    """

    # Formula ensures that the coordinates fall within game window
    x = int(random.randint(0, 399)/20)*20
    y = int(random.randint(0, 299)/20)*20

    return x, y


# Initializes the pygame library
pg.init()

# Sets the size of the window/cell
winSize = (400, 300)
window = pg.display.set_mode(winSize)
cellSize = 20

# Sets the title of the window
pg.display.set_caption('Snake Game')

# The clock will be used to control how fast the screen updates
clock = pg.time.Clock()

# Loads start/end screens
startscreen = pg.image.load('snake_game_start.jpg')
endscreen = pg.image.load('snake_game_gameover.jpg')

# Sets start point
wormCoords = [{'x': 5, 'y': 5},
              {'x': 5, 'y': 4},
              {'x': 5, 'y': 3}]

# Sets starting direction of worm and starting position of apple
direction = 'right'
apple_x, apple_y = randCoord()

# Initializes boolean variables
standby = True
start = True
end = True


while standby:  # start screen
    window.fill((255, 64, 64))
    window.blit(startscreen, (0, 0))
    pg.display.flip()
    for event in pg.event.get():
        if event.type is MOUSEBUTTONDOWN:
            standby = False
        elif event.type is QUIT:
            pg.quit()
            sys.exit()

while start:  # main game loop
    for event in pg.event.get():
        if event.type is QUIT:
            pg.quit()
            sys.exit()

    if 'x' == 19 and direction is 'right':
        direction = 'down'
    elif 'x' == 0 and direction is 'left':
        direction = 'up'
    elif 'y' == 14 and direction is 'down':
        direction = 'left'
    elif 'y' == 0 and direction is 'up':
        direction = 'right'

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and direction is not 'right':
        direction = 'left'
    if keys[pg.K_RIGHT] and direction is not 'left':
        direction = 'right'
    if keys[pg.K_UP] and direction is not 'down':
        direction = 'up'
    if keys[pg.K_DOWN] and direction is not 'up':
        direction = 'down'


    if direction is 'up':
        newHead = {'x': wormCoords[0]['x'], 'y': wormCoords[0]['y'] - 1}
    elif direction is 'down':
        newHead = {'x': wormCoords[0]['x'], 'y': wormCoords[0]['y'] + 1}
    elif direction is 'left':
        newHead = {'x': wormCoords[0]['x'] - 1, 'y': wormCoords[0]['y']}
    else:
        newHead = {'x': wormCoords[0]['x'] + 1, 'y': wormCoords[0]['y']}


    window.fill((255, 255, 255))
    drawGrid(window, winSize, cellSize, (40, 40, 40))
    drawWorm(window, wormCoords, cellSize, (225, 0, 0))
    drawApple(window, cellSize, (0, 255, 0), apple_x, apple_y)

    if newHead['x']*20 != apple_x or newHead['y']*20 != apple_y:
        del wormCoords[-1]  # remove worm's tail segment
        wormCoords.insert(0, newHead)
    else:
        apple_x, apple_y = randCoord()
        wormCoords.insert(0, newHead)

    # --- Game Over conditions
    if newHead['x'] < 0\
            or newHead['x'] > winSize[0]/cellSize - 1\
            or newHead['y'] < 0\
            or newHead['y'] > winSize[1]/cellSize - 1:  # Cannot touch wall
                start = False
    for i, c in enumerate(wormCoords):  # Cannot touch body
        if i != 0:
            if newHead == c:
                start = False

    # --- Go ahead and update the screen with what we've drawn.
    pg.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(5)

while end:  # game over screen
    window.fill((255, 64, 64))
    window.blit(endscreen, (0, 0))
    pg.display.flip()
    for event in pg.event.get():
        if event.type is MOUSEBUTTONDOWN:
            end = False
        elif event.type is QUIT:
            pg.quit()
            sys.exit()
