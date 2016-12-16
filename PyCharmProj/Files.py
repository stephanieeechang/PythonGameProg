'''
Lists all the files inside a folder.
If there is a folder inside, the function is called recursively to list the files inside
'''
import os

def displayFiles():
    folder = input('Which folder? ')
    return displayFiles()
