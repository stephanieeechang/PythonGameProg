'''
The program finds out the average of the user's input
'''

vInput = 0
vAcc = 0
iter = 0

while(type(vInput) is int):
    vInput = input('Enter your value (0~100), any letter to finalize: ')
    if (vInput >= 0 and vInput <= 100):
        vAcc += vInput
        iter += 1
        print(vAcc/iter)
print(vAcc/iter)
