'''
The program finds out the average of the user's input
(uses a while loop with a for loop)
'''

vInput = 0
vAcc = 0
iter = 0

vInput = input('Enter your value (0~100), any letter to finalize: ')

for vInput in int:
    vInput = input('Enter your value (0~100), any letter to finalize: ')
    while(vInput >= 0 and vInput <= 100):
        iter += 1
        print(vAcc/iter)
print(vAcc/iter)
