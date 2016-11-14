'''
main python file
'''
import stafflib as slib

employee = slib.newEmployee('John', 'Sena', '30', '11-Nov-2016', '1000', 'driver')
employee = slib.newEmployee('John', 'Smith', '35', '12-Nov-2016', '900', 'co-driver')
employee = slib.newEmployee('Alice', 'Anderson', '38', '18-Dec-2015', '1800', 'treasurer')
employee = slib.newEmployee('Wilson', 'Hu', '31', '5-Aug-2016', '2200', 'chief legal officer')
employee = slib.newEmployee('Eason', 'Sugg', '40', '25-Nov-2015', '7500', 'president')
employee = slib.deleteEmployee(employee)

days = slib.incrementDay()

slib.showCurrentEmployee(employee, days)
