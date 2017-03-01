import pygame as pg
import sys
from pygame.locals import *

# Initializes the pygame library
pg.init()

# Sets the size of the window/cell
winSize = (400, 650)
window = pg.display.set_mode(winSize)

# The clock will be used to control how fast the screen updates
clock = pg.time.Clock()

# read game images: sprites
red = pg.image.load('traffic_red.png')
green = pg.image.load('traffic_green.png')
yellow = pg.image.load('traffic_yellow.png')
off = pg.image.load('traffic_off.png')

traffic = {'pos_x' : 80, 'pos_y' : 0,
           'red':red, 'yellow':yellow,
           'green':green, 'off':off}

state = {'state' : 'off', 'counter' : 0}
a, b = 0, 0

while True:  # main game loop
    for event in pg.event.get():
        if event.type is QUIT:
            pg.quit()
            sys.exit()
    keys = pg.key.get_pressed()

    window.fill((255,255,255))
    # press [SPACE] to start
    if keys[pg.K_SPACE]:
        state['state'] = 'red' if state['state'] is 'off' else 'off'

    if state['state'] is 'off':
        case_rect = pg.Rect(traffic['pos_x'], traffic['pos_y'], 10, 10)
        window.blit(traffic['off'], case_rect)

    elif state['state'] is 'red':
        # print a rectangle
        red_rect = pg.Rect(traffic['pos_x'], traffic['pos_y'], 50, 50)
        # replace rectangle with image
        window.blit(traffic['red'], red_rect)
        # transmition
        state['counter'] += 1
        if state['counter'] >= 10:
            state['state'] = 'green'
            state['counter'] = 0
        else:
            state['state'] = 'red'

    elif state['state'] is 'yellow':
        # print a rectangle
        yellow_rect = pg.Rect(traffic['pos_x'], traffic['pos_y'], 50, 50)
        # replace rectangle with image
        window.blit(traffic['yellow'], yellow_rect)
        # transmition
        state['counter'] += 1
        if state['counter'] >= 10:
            state['state'] = 'red'
            state['counter'] = 0
        else:
            state['state'] = 'yellow'

    elif state['state'] is 'green':
        # print a rectangle
        green_rect = pg.Rect(traffic['pos_x'], traffic['pos_y'], 50, 50)
        # replace rectangle with image
        window.blit(traffic['green'], green_rect)
        # transmition
        state['counter'] += 1
        if state['counter'] >= 10:
            state['state'] = 'yellow'
            state['counter'] = 0
        else:
            state['state'] = 'green'


    # --- Go ahead and update the screen with what we've drawn.
    pg.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(10)
