'''
Q2 final project
Codingame - Easy Level - Temperatures
'''
while True:
    highest = -1
    index = -1
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain, from 9 to 0.
        if mountain_h > highest:
            highest = mountain_h
            index = i

    # The number of the mountain to fire on.
    print(index)
