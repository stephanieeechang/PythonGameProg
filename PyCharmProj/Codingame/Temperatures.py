'''
Q2 final project
Codingame - Easy Level - Temperatures
'''
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temps = input()  # the n temperatures expressed as integers ranging from -273 to 5526

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
tempList = temps.split(" ")
high = 0
for i in range(1, n):
    if abs(int(tempList[high])) > abs(int(tempList[i])):
        high = i
    elif abs(int(tempList[high])) == abs(int(tempList[i])):
        if int(tempList[high]) < int(tempList[i]):
            high = i
if temps[high] == "":
    tempList(0)
else:
    print(tempList[high])
