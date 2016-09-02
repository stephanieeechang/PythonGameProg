'''
The program translates a point score (0-100) to a letter grade (A+, A, etc)

The point score is passed as an argument to the script in the terminal
'''


import sys
print('The point score is: ')
print(sys.argv)

score = float(sys.argv[1]) #argument
letterGrade = 'A+'

if score <= 100 and score >= 97:
    letterGrade = 'A+'
elif score <= 96 and score >= 93:
    letterGrade = 'A'
elif score <= 92 and score >= 90:
    letterGrade = 'A-'
elif score <= 89 and score >= 87:
    letterGrade = 'B+'
elif score <= 86 and score >= 83:
    letterGrade = 'B'
elif score <= 82 and score >= 80:
    letterGrade = 'B-'
elif score <= 79 and score >= 77:
    letterGrade = 'C+'
elif score <= 76 and score >= 73:
    letterGrade = 'C'
elif score <= 72 and score >= 70:
    letterGrade = 'C-'
elif score <= 69 and score >= 67:
    letterGrade = 'D+'
elif score <= 66 and score >= 63:
    letterGrade = 'D'
elif score <= 62 and score >= 60:
    letterGrade = 'D-'
elif score <= 59 and score >= 0:
    letterGrade = 'F'
else:
    print('Please enter a valid grade!')
    letterGrade = 'Error!'


print('The letter grade is ')
print(letterGrade)
