'''
Get a list of txt files in a directory using a list comprehension
'''
import os
fileList = os.listdir(os.path.expanduser('~/Desktop/Python/PythonGameProg/PyCharmProj'))

txtFile = [f for f in fileList if f.endswith('.txt')]
print txtFile
