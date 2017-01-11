'''
Q2 final project
Codingame - Easy Level - Mime Type
'''
import sys

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
mimeDict = {}
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    mimeDict[ext.lower()] = mt

for i in range(q):
    fname = input()  # One file name per line.
    print(fname, file=sys.stderr)
    if '.' in fname:
        fileName, extension = fname.rsplit('.',1)
        if extension.lower() in mimeDict:
            print(mimeDict[extension.lower()])
        else:
            print("UNKNOWN")
    else:
        print("UNKNOWN")

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.

