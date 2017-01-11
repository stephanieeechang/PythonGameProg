'''
Q2 final project
Codingame - Easy Level - Chuck Norris
'''
message = input()
binMsg = []

for x in message:
    # converts c to a 7digit 0 left padded binary code
    binMsg.append('{0:07b}'.format(ord(x)))

decrypted = ""
previous = ""
count = 0
for letter in ''.join(binMsg):
    if letter != previous:
        for i in range(count):
            decrypted += '0'
        if count > 0:
            decrypted += ' '
        if letter == '0':
            decrypted += "00 "
        else:
            decrypted += "0 "
        count = 1
    else:
        count += 1

    previous = letter
decrypted += '0'*count

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(decrypted)
