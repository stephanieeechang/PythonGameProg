'''
Q2 final project
Codingame - Easy Level - Horse-racing Duals
'''
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
piList = []
smallest = 9999
difference = 999
for i in range(n):
    pi = int(input())
    piList.append(pi)
piList.sort()

for a in range(len(piList)-1):
    difference = abs(piList[a] - piList[a+1])
    if difference < smallest:
        smallest = difference

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(smallest)
