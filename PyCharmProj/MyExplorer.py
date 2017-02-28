import pygame as pg
import sys

from pygame.locals import *

# initialize the pygame library
pg.init()
# sets the size of the window
winSize = (800, 700)
window = pg.display.set_mode(winSize)
# title
pg.display.set_caption('Walking Machine')
# The clock will be used to control how fast the screen updates
clock = pg.time.Clock()

# load images
wait = pg.image.load('KrustyWait.png')
downwalk1 = pg.image.load('KrustyDownWalk1.png')
downwalk2 = pg.image.load('KrustyDownWalk2.png')
downwalk3 = pg.image.load('KrustyDownWalk3.png')
downwalk4 = pg.image.load('KrustyDownWalk4.png')
upwalk = pg.image.load('KrustyUpWalk.png')
leftwalk1 = pg.image.load('KrustyLeftWalk1.png')
leftwalk2 = pg.image.load('KrustyLeftWalk2.png')
leftwalk3 = pg.image.load('KrustyLeftWalk3.png')
leftwalk4 = pg.image.load('KrustyLeftWalk4.png')
rightwalk1 = pg.image.load('KrustyRightWalk1.png')
rightwalk2 = pg.image.load('KrustyRightWalk2.png')
rightwalk3 = pg.image.load('KrustyRightWalk3.png')
rightwalk4 = pg.image.load('KrustyRightWalk4.png')

scaleWait = pg.transform.scale(wait, (66, 105))
scaleDWalk1 = pg.transform.scale(downwalk1, (66, 105))
scaleDWalk2 = pg.transform.scale(downwalk2, (66, 105))
scaleDWalk3 = pg.transform.scale(downwalk3, (66, 105))
scaleDWalk4 = pg.transform.scale(downwalk4, (66, 105))
scaleLWalk1 = pg.transform.scale(leftwalk1, (66, 105))
scaleLWalk2 = pg.transform.scale(leftwalk2, (66, 105))
scaleLWalk3 = pg.transform.scale(leftwalk3, (66, 105))
scaleLWalk4 = pg.transform.scale(leftwalk4, (75, 105))
scaleRWalk1 = pg.transform.scale(rightwalk1, (75, 105))
scaleRWalk2 = pg.transform.scale(rightwalk2, (66, 105))
scaleRWalk3 = pg.transform.scale(rightwalk3, (66, 105))
scaleRWalk4 = pg.transform.scale(rightwalk4, (66, 105))
scaleUWalk = pg.transform.scale(upwalk, (66, 105))


# dictionary for the character
felix = {
    'pos_x':int(winSize[0]/2),
    'pos_y':int(winSize[1]/2),
    'wait':scaleWait,
    'downwalk1':scaleDWalk1,
    'downwalk2':scaleDWalk2,
    'downwalk3':scaleDWalk3,
    'downwalk4':scaleDWalk4,
    'leftwalk1':scaleLWalk1,
    'leftwalk2':scaleLWalk2,
    'leftwalk3':scaleLWalk3,
    'leftwalk4':scaleLWalk4,
    'rightwalk1':scaleRWalk1,
    'rightwalk2':scaleRWalk2,
    'rightwalk3':scaleRWalk3,
    'rightwalk4':scaleRWalk4,
    'upwalk':scaleUWalk
}

# dictionary for the state machine
state = {'state':'wait', 'param':{}, 'image':'wait'}
walk = 10

while True:  # main game loop
    for event in pg.event.get():
        if event.type is QUIT:
            pg.quit()
            sys.exit()
    keys = pg.key.get_pressed()

    window.fill((255, 255, 255))

    if state['state'] is 'wait':
        # output
        state['image'] = 'wait'
        # transition
        if keys[pg.K_DOWN]:
            state['state'] = 'dwalk'
            state['param'] = {'time':0}
        elif keys[pg.K_LEFT]:
            state['state'] = 'lwalk'
            state['param'] = {'time':0}
        elif keys[pg.K_RIGHT]:
            state['state'] = 'rwalk'
            state['param'] = {'time':0}
        elif keys[pg.K_UP]:
            state['state'] = 'uwalk'
            state['param'] = {'time':0}

    elif state['state'] is 'dwalk':
        # output
        t = state['param']['time']
        n = t%4+1
        state['image'] = 'downwalk' + str(n)
        felix['pos_y'] += walk
        # transition
        if keys[pg.K_DOWN]:
            state['param']['time'] += 1
        else:
            state['state'] = 'wait'

    elif state['state'] is 'lwalk':
        # output
        t = state['param']['time']
        n = t%4+1
        state['image'] = 'leftwalk' + str(n)
        felix['pos_x'] -= walk
        # transition
        if keys[pg.K_LEFT]:
            state['state'] = 'lwalk'
            state['param']['time'] += 1
        else:
            state['state'] = 'wait'

    elif state['state'] is 'rwalk':
        # output
        t = state['param']['time']
        n = t%4+1
        state['image'] = 'rightwalk' + str(n)
        felix['pos_x'] += walk
        # transition
        if keys[pg.K_RIGHT]:
            state['param']['time'] += 1
        else:
            state['state'] = 'wait'

    elif state['state'] is 'uwalk':
        # output
        t = state['param']['time']
        state['image'] = 'upwalk'
        felix['pos_y'] -= walk
        # transition
        if keys[pg.K_UP]:
            state['param']['time'] += 1
        else:
            state['state'] = 'wait'

    felix_rect = pg.Rect(felix['pos_x'], felix['pos_y'], 50, 50)
    image = state['image']
    window.blit(felix[image], felix_rect)
    # --- Go ahead and update the screen with what we've drawn.
    pg.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(10)
