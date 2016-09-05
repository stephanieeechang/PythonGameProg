'''
The program determines what kind of ticket the user is getting from the speed he/she drives and his/her birthday

user inputs the speed and if the day is his/hers birthday
'''

speed = input('Input the speed you are driving: ')
birthday = input('Is today your birthday? (yes or no): ')

if birthday == 'yes':
    if speed <= 60:
        print('No ticket.')
    elif speed <=80 and speed >= 61:
        print('Small ticket.')
    elif speed >= 81:
        print('Big ticket.')
elif birthday == 'no':
    if speed <= 65:
        print('No ticket.')
    elif speed <=85 and speed >= 66:
        print('Small ticket.')
    elif speed >= 86:
        print('Big ticket.')
