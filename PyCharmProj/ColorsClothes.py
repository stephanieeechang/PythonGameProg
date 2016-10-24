'''
generates different combinations of clors and clothes
'''

colors = ['red', 'yellow', 'blue']
clothes = ['hat', 'shirt', 'pants']
combination = [i + ' ' + j for i in colors for j in clothes]
print combination
