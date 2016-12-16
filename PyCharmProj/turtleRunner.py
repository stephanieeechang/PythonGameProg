import turtle

def square(sqrlength, turtle):
    '''
    this function draws a square with turtle
    :param sqrlength: length of square
    :return:
    '''
    if sqrlength < 5:
        return
    else:
        for i in range(4):
            turtle.forward(sqrlength)
            turtle.left(90)
        turtle.up()
        turtle.fd(5)
        turtle.left(90)
        turtle.fd(5)
        turtle.left(-90)
        turtle.down()

        square(sqrlength-10, turtle)


def tree(tur, times, len):
    if(times != 1):
        tur.fd(len)
        tur.right(20)
        tree(tur, times-1, len-10)
        tur.left(40)
        tree(tur, times-1, len-10)
        tur.right(20)
        tur.backward(len)


myWin = turtle.Screen()
#creates a turtle
rp = turtle.Turtle()
#draw a square
#square(100, rp)
#draw a tree
rp.up()
rp.back(80)
rp.down()
rp.left(90)
tree(rp, 8, 80)
#close window by clicking screen
myWin.exitonclick()
