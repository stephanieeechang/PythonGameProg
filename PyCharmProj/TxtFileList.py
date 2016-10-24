'''
Get a list of txt files in a directory using a list comprehension
'''
import os
txtList = os.listdir(os.path.expanduser('~/Desktop/Python/PythonGameProg/PyCharmProj'))

for f in txtList:
    print f
