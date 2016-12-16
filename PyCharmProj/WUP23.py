'''
WUP #23 programs
'''
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

# email = input('Enter an e-mail address: ')
# print(checkEmail(email))


def checkDate(date):
    if date[:3].isDigit() == True and date[4] == '-' and date[5:7].isDigit() == True and date[7] == '-' and date[8:]:
        return True
    else:
        return False

date = input('Enter a date in the yyyy-mm-dd format: ')
checkDate(date)
