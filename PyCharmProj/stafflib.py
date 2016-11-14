'''
python library
'''

data = {'firstName':'', 'lastName':'' , 'age':'', 'employedSince':'' , 'role':'' , 'daysWorked':'', 'salary':''}
employeeList = []

def newEmployee(fn, ln, age, since, salary, role):
    '''
    store the information of an employee (receive inputs)
    :param fn: first name
    :param ln: last name
    :param age: age
    :param since: employed since (d-m-y)
    :param salary: salary
    :param role: role
    :return employeeList: a list with all information of employee(s)
    '''
    dataC = data.copy()
    dataC['firstName'] = fn
    dataC['lastName'] = ln
    dataC['age'] = age
    dataC['employedSince'] = since
    dataC['role'] = role
    dataC['salary'] = salary
    employeeList.append(dataC)
    print employeeList
    return employeeList


def showCurrentEmployee(eList, day):
    '''
    prints out the information of all current employees
    :param eList: a list with all information of employee(s)
    :param day: a list of days the employees have worked
    :return: None
    '''
    count = 1
    print('Showing registre of employees:')
    for i in eList:
        print('Staff#' + str(count))
        print(i['firstName'] + ' ' + i['lastName'] + ', age ' + i['age'] + ', has been working for ' + str(day[count-1]) +
              ' day since ' + i['employedSince'] + ' as a ' + i['role'] + ' for USD' + i['salary'])
        count += 1
    print('Task completed.')


def incrementDay():
    '''
    increments the days of the employees have worked
    :return:
    '''
    days = [3, 2, 333, 102, 356]
    newDay = raw_input('New day? (y/n): ')
    if(newDay == 'y'):
        count = 0
        for i in days:
            i+=1
            days[count] = i
            count += 1
    return days


def deleteEmployee(eList):
    '''
    deletes an employee from the list
    :param eList: a list with all information of employee(s)
    :return eList: a list with all information of employee(s)
    '''
    which = input('Which employee do you want to delete? (number): ')
    eList.pop(which-1)
    return eList
