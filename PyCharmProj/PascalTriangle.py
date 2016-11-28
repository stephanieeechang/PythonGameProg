'''
draw the pascal triangle
'''

def triangle(final):
    for r in range(final):
        num = ''
        for c in range(r+1):
            num = num + str(count(r, c)) + "\t"
        print num

def count(row, column):
    if column == 0:
        return 1
    if row == 0:
        return column
    else:
        return (row * count(row-1, column-1)) / column

rows = input('How many rows of the pascal triangle would you like to display? ')
triangle(rows)
