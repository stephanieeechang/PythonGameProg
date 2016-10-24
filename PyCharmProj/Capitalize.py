'''
The program capitalizes a list of words
'''

words = ['ALICE', 'bob', 'Python', 'john', 'a', 'alice']
temporary = []

caplist = [i[0].upper() + i[1:].lower() for i in words if len(i) > 2]

if i not in temporary:
    temporary.append(i)

print caplist
