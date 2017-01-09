'''
the program reads a GoogleClassroom csv file and creates a csv in the format of the PowerSchool system
'''
import csv
import datetime
psDict = {'Teacher Name:':'', 'Section:':'Python', 'Assignment Name:':'',
          'Due Date:':'', 'Points Possible:':'10', 'Extra Points:':'0', 'Score Type:':'Points',
          'Student ID':'', 'Student Name':'', 'Points':''}
print('1-Read Google Classroom file')

#open the file
gcFile = open('GoogleActivities.csv')
gcData = csv.reader(gcFile)
#show all the rows in the file
gcdata = []
for count, row in enumerate(gcData):
    print(count+1, row)
    gcdata.append(row)

#activities (assignments)
gcNum = len(gcdata[0])-3
print('Number of activities found:', gcNum)
actList = []
for num, activities in enumerate(gcdata[0]):
    if num > 2:
        actList.append(activities)
        print('Activity', num-2, ':', activities)
print('')
psDict['Assignment Name:'] = actList

#due date
dateList = []
week = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
         'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
dateStr = ''
for num, date in enumerate(gcdata[1]):
    if num > 2:
        for m in range(len(month)):
            if date[3:6] == month[m]:
                numMonth = m+1
        day = week[datetime.datetime(int('20'+date[-2:]),numMonth,int(date[:2])).weekday()]
        dateStr += day + ' ' + date[3:6] + ' ' + date[:2] + ' ' + '00:00:00 CST' + ' 20'+date[-2:]
        dateList.append(dateStr)
        dateStr = ''
psDict['Due Date:'] = dateList

#students' names
name = ''
names = []
for i, row in enumerate(gcdata):
    if i > 2:
        print('Student', i-2, ':' , row[1], row[0])
        names.append(row[1] + ', ' + row[0])
print(names, '\n')
psDict['Student Name'] = names

#score
scoreList = []
for asg in range(len(names)):
    for n, score in enumerate(gcdata[gcNum+3]):
        if n > 2:
            scoreList.append(int(int(score)*0.1))
psDict['Points'] = scoreList

#close file
gcFile.close()

#########################################################
print('\n2-Read PowerSchool file')

#open the file
psFile = open('PowerSchool Template.csv')
psData = csv.reader(psFile)
#show all the rows in the file
psdata = []
for count, row in enumerate(psData):
    print(count+1, row)
    psdata.append(row)

#teacher's name
for t, row in enumerate(psdata[0]):
    if t == 1:
        psDict['Teacher Name:'] = row

#section
for s, row in enumerate(psdata[1]):
    if s == 1:
        psDict['Section:'] = row

#student ID
stuIDList = []
for i, row in enumerate(psdata):
    if i > 8:
        for num, id in enumerate(psdata[i]):
            if num == 0:
                stuIDList.append(id)
psDict['Student ID'] = stuIDList

#close file
psFile.close()

def gc_ps(num):
    '''
    write all datas from the PowerSchool dictionary to .csv files in the PowerSchool format
    :param num: int (number of assignments)
    :return: none
    '''
    for i in range(num):
        newPS = open(psFileName(i+1), 'w')
        writer = csv.writer(newPS, delimiter=',')
        writer.writerow(['Teacher Name:'] + [psDict['Teacher Name:']])
        writer.writerow(['Section:']+[psDict['Section:']])
        for n, a in enumerate(psDict['Assignment Name:']):
            if n == i:
                writer.writerow(['Assignment Name:']+[a])
        for n, d in enumerate(psDict['Due Date:']):
            if n == i:
                writer.writerow(['Due Date:']+[d])
        writer.writerow(['Points Possible']+ [psDict['Points Possible:']])
        writer.writerow(['Extra Points:']+[psDict['Extra Points:']])
        writer.writerow(['Score Type:']+[psDict['Score Type:']])
        writer.writerow('')
        writer.writerow(['Student ID']+ ['Student Name']+ ['Points'])
        for n in range(len(psDict['Student ID'])):
            writer.writerow([psDict['Student ID'][n]]+ [psDict['Student Name'][n]]+ [psDict['Points'][(4*n)+i]])
        newPS.close()

def psFileName(num):
    '''
    create filenames according to the number of assignments
    :param num: int (number of assignments)
    :return: filename
    '''
    name = 'Assignment'
    name += str(num) + '.csv'
    return name

gc_ps(gcNum)
print(psDict)
