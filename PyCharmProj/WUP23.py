'''
WUP #23 programs
'''
import re

def checkEmail(email):
    notValid = '!#$%^&*()-+=~:";\\|{}[]\'<>,/?`@ '
    if '@' in email:
        email = email.replace('@', '', 1)
        print(email)
    else:
        return False

    count = 0
    for letter in email:
        if letter in notValid:
            return False
        if letter == '@':
            position = count
            if '.' not in email[position:]:
                return False
        count += 1
    return True

def regexCheckEmail(email):
    result = re.match(r'(\w+[.|\w])*@(\w+[.])*\w+', email)
    if result != None:
        valid = True
    else:
        valid = False
    if valid:
        return email + " is a valid e-mail."
    else:
        return email + " is not a valid e-mail."

email = input('Enter an e-mail address: ')
print(regexCheckEmail(email))

def regexCheckDate(date):
    result = re.match(r'(\d{4})[-](\d{2})[-](\d{2})', date)
    if result != None:
        valid = True
    else:
        valid = False
    if valid:
        return date + " is a date in the yyyy-mm-dd format."
    else:
        return date + " is not a date in the yyyy-mm-dd format."

date = input('Enter a date in the yyyy-mm-dd format: ')
print(regexCheckDate(date))
