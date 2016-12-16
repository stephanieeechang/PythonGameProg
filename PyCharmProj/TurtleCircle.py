import turtle
import colorsys
###################Library################

def drawcircle(x, y, radius, t):
    '''
    draws a circle
    :param x: initial x coordinate
    :param y: initial y coordinate
    :param radius: the radius of the circle
    :param t: turtle
    :return: none
    '''
    moveturtle(x+radius, y+radius)
    # pen color
    (r, g, b) = colorsys.hsv_to_rgb(float(radius) / 150, 1.0, 1.0)
    t.pencolor(r, g, b)
    # draw circle
    t.circle(radius)
    # return to the initial position
    moveturtle(x, y)
    # smaller circles
    if radius > 10:
        drawcircle(x+radius, y+radius, radius/2, t)
        drawcircle(x-radius, y-radius, radius/2, t)


def moveturtle(x, y):
    '''
    moves the turtle to a desired coordinate
    :param x: x coordinate
    :param y: y coordinate
    :return: none
    '''
    t.up()
    t.setposition(x, y)
    t.down()
#######################################


t = turtle.Turtle()
t.pensize(2)
moveturtle(-50, 0)
myWin = turtle.Screen()
drawcircle(x=1, y=100, radius=90,t=t)
myWin.exitonclick()
