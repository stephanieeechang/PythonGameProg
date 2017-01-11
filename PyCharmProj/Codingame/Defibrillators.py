'''
Q2 final project
Codingame - Easy Level - Defibrillators
'''
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

defibList = []
smallestD = 99999999
lon = input()
lon = float(lon.replace(',','.'))*math.pi/180
lat = input()
lat = float(lat.replace(',','.'))*math.pi/180
n = int(input())
for i in range(n):
    defib = input()
    dSplit = defib.split(';')
    dSplit[4] = float(dSplit[4].replace(',','.'))*math.pi/180
    dSplit[5] = float(dSplit[5].replace(',','.'))*math.pi/180
    x = (dSplit[4]-lon)*math.cos((lat+dSplit[5])/2)
    y = dSplit[5]-lat
    d = math.sqrt(x**2 + y**2)*6371
    if d < smallestD:
        smallestD = d
        name = dSplit[1]

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(name)
