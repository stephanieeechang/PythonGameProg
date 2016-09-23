'''
The program prints the numbers that are divisible by 7 and multiple of 5, between 1500 and 2700
'''

for i in range(1500, 2701):
    if not (i%7 or i%5):
        continue
    print(i)
