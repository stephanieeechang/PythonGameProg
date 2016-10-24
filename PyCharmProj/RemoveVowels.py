'''
removes all vowels from a sentence
'''

sentence = 'Your mother was a hamster'
new = [x for x in sentence if x not in 'aeiou']
newSen = ''
for i in new:
    newSen += i
print newSen
