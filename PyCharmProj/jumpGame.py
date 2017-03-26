'''
jump upwards without hitting any obstacles
'''

import pygame as pg
import sys
import random
from pygame.locals import *

# initialize the pygame library
pg.init()
# sets the size of the window
winSize = (530, 800)
width = winSize[0]
height = winSize[1]
window = pg.display.set_mode(winSize)
# title
pg.display.set_caption('Jump!')
# The clock will be used to control how fast the screen updates
clock = pg.time.Clock()

leftFly = pg.image.load('doodleLeft.png')
rightFly = pg.image.load('doodleRight.png')
monster1 = pg.image.load('monster1.png')
monster2 = pg.image.load('monster2.png')
monster3 = pg.image.load('monster3.png')
monster4 = pg.image.load('monster4.png')
monster5 = pg.image.load('monster5.png')
startscreen = pg.image.load('doodleStart.jpg')
endscreen = pg.image.load('doodleGameover.png')
background = pg.image.load('doodleBackground.png')
backgroundWidth, backgroundHeight = background.get_size()

scaleL = pg.transform.scale(leftFly, (139, 130))
scaleR = pg.transform.scale(rightFly, (139, 130))
scaleM1 = pg.transform.scale(monster1, (77, 77))
scaleM2 = pg.transform.scale(monster2, (93, 47))
scaleM3 = pg.transform.scale(monster3, (90, 59))
scaleM4 = pg.transform.scale(monster4, (76, 82))
scaleM5 = pg.transform.scale(monster5, (97, 54))
scaleStart = pg.transform.scale(startscreen, (width, height))
scaleEnd = pg.transform.scale(startscreen, (width, height))
scaleBg = pg.transform.scale(background, (width, height))
doodleWidth, doodleHeight = scaleL.get_size()

# dictionary for the character
doodle = {
    'pos_x':int(winSize[0]/2),
    'pos_y':int(winSize[1]/2),
    'leftf':scaleL,
    'rightf':scaleR
}

monster1 = {
    'pos_x':random.randint(0, width),
    'pos_y':1000,
    'm1':scaleM1,
    'm2':scaleM2,
    'm3':scaleM3,
    'm4':scaleM4,
    'm5':scaleM5
}

monster2 = {
    'pos_x':random.randint(0, width),
    'pos_y':1000,
    'm1':scaleM1,
    'm2':scaleM2,
    'm3':scaleM3,
    'm4':scaleM4,
    'm5':scaleM5
}

monster3 = {
    'pos_x':random.randint(0, width),
    'pos_y':1000,
    'm1':scaleM1,
    'm2':scaleM2,
    'm3':scaleM3,
    'm4':scaleM4,
    'm5':scaleM5
}

state = {'state':'wait', 'image':'wait'}
mons1 = {'posX':0, 'posY':0, 'image':'m1'}
mons2 = {'posX':0, 'posY':0, 'image':'m1'}
mons3 = {'posX':0, 'posY':0, 'image':'m1'}
fly = 10
monsDown = 3

def randomMonster(x, y, monster, mNum):
    monster_rect = pg.Rect(x, y, 100, 100)
    image = mNum
    window.blit(monster[image], monster_rect)
    return monster_rect


# Initialize condition
standby = True
start = True
end = True

while standby:  # start screen
    window.fill((255, 64, 64))
    window.blit(scaleStart, (0, 0))
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

    backgroundRect = pg.Rect(0, 0, 50, 50)
    window.fill((255, 255, 255))
    window.blit(background, backgroundRect)

    keys = pg.key.get_pressed()

    if state['state'] is 'wait':
        # output
        if doodle['pos_x'] <= int(winSize[0]/2):
            state['image'] = 'leftf'
        elif doodle['pos_x'] > int(winSize[0]/2):
            state['image'] = 'rightf'
        # transition
        if keys[pg.K_LEFT]:
            state['state'] = 'lfly'

        elif keys[pg.K_RIGHT]:
            state['state'] = 'rfly'

    elif state['state'] is 'lfly':
        # output
        state['image'] = 'leftf'
        doodle['pos_x'] -= fly
        # transition
        if keys[pg.K_LEFT]:
            state['state'] = 'lfly'
        else:
            state['state'] = 'wait'

        if doodle['pos_x'] < 0:
            doodle['pos_x'] = width
            state['state'] = 'lfly'

    elif state['state'] is 'rfly':
        # output
        state['image'] = 'rightf'
        doodle['pos_x'] += fly
        # transition
        if keys[pg.K_RIGHT]:
            state['state'] = 'rfly'
        else:
            state['state'] = 'wait'

        if doodle['pos_x'] > width-doodleWidth:
            doodle['pos_x'] = 0
            state['state'] = 'rfly'

    else:
        state['state'] = 'wait'

    doodle_rect = pg.Rect(doodle['pos_x'], doodle['pos_y'], 50, 50)
    doodleImage = state['image']
    window.blit(doodle[doodleImage], doodle_rect)

    # generate monster1
    if monster1['pos_y'] > height: # if monster goes off screen
        monster1['pos_x'] = random.randint(0, width)
        monster1['pos_y'] = random.randint(0, doodle['pos_y']-100)
        monsNum1 = 'm' + str(random.randint(1, 5))
        mons1_rect = randomMonster(monster1['pos_x'], monster1['pos_y'], monster1, monsNum1)

    else:
        monster1['pos_y'] += monsDown
        randomMonster(monster1['pos_x'], monster1['pos_y'], monster1, monsNum1)

    # generate monster2
    if monster2['pos_y'] > height: # if monster goes off screen
        monster2['pos_x'] = random.randint(0, width)
        monster2['pos_y'] = random.randint(0, doodle['pos_y']-100)
        monsNum2 = 'm' + str(random.randint(1, 5))
        mons2_rect = randomMonster(monster2['pos_x'], monster2['pos_y'], monster2, monsNum2)

    else:
        monster2['pos_y'] += monsDown
        randomMonster(monster2['pos_x'], monster2['pos_y'], monster2, monsNum2)

    # generate monster3
    if monster3['pos_y'] > height: # if monster goes off screen
        monster3['pos_x'] = random.randint(0, width)
        monster3['pos_y'] = random.randint(0, doodle['pos_y']-100)
        monsNum3 = 'm' + str(random.randint(1, 5))
        mons3_rect = randomMonster(monster3['pos_x'], monster3['pos_y'], monster3, monsNum3)

    else:
        monster3['pos_y'] += monsDown
        randomMonster(monster3['pos_x'], monster3['pos_y'], monster3, monsNum3)

    # game over
    if doodle_rect.colliderect(mons1_rect) or doodle_rect.colliderect(mons2_rect) \
            or doodle_rect.colliderect(mons3_rect):
        start = False

    # --- Go ahead and update the screen with what we've drawn.
    pg.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(20)

while end:  # game over screen
    window.fill((255, 64, 64))
    window.blit(scaleEnd, (0, 0))
    pg.display.flip()
    for event in pg.event.get():
        if event.type is MOUSEBUTTONDOWN:
            end = False
        elif event.type is QUIT:
            pg.quit()
            sys.exit()
