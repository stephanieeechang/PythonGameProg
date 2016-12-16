zen_message = 'Simple is worst than complex'
i = zen_message.find('worst')
zen = ''
for x in range(i, i+len('worst')):
    zen += zen_message[x]
print(zen)
print(zen_message)

'''
Use the methods isalnum(), isalpha(), isdecimal(), and len() to create a program for validating passwords.
The program asks the user for a new password and terminates only when the user enters a correct password.
The minimum length of the password is 8 characters and must include only letters and numbers. At least one number.

password = raw_input('Enter your password: ')
while password.isdecimal() or password.isalpha() or len(password) < 8:
    password = raw_input('Enter your password: ')
print password
'''


print('*'.join(zen_message.split()))
