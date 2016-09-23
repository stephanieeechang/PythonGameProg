'''
The program constructs the following pattern:
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''

for i in range(1, 6):
    print('*'*i)
for j in range(1, 5):
    print('*'*(5-j))
