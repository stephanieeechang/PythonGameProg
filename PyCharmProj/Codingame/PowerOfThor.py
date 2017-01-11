'''
Q2 final project
Codingame - Easy Level - Power Of Thor
'''
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
thorX=initial_tx
thorY=initial_ty
# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    directionX=""
    directionY=""
    if thorY>light_y:
        directionY+="N"
        thorY-=1
    elif thorY<light_y:
        directionY+="S"
        thorY+=1
    if thorX>light_x:
        directionX+="W"
        thorX+=1
    elif thorX<light_x:
        directionX+="E"
        thorX-=1

    print(directionY+directionX)
