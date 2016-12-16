'''
English to Spanish dictionary
'''

eng2spa = {'one':'uno', 'two':'dos', 'three':'tres', 'four':'cuatro', 'five':'cinco',
           'six':'seis', 'seven':'siete', 'eight':'ocho', 'nine':'nueve', 'ten':'diez'}

#print the keys in eng2spa
print(eng2spa.keys())

#check if a word is in a dictionary
print('once' in eng2spa)

#try all dict methods (del, clear, copy, fromkeys, get, items, keys, values)
eng2spa.__delitem__('one')
print('\n\tafter del: ')
print(eng2spa.keys())
print(eng2spa.values())
print(eng2spa.items())

eng2spa.copy()

newdic = {}
seq = ('name', 'age', 'sex')
printdic = newdic.fromkeys(seq, 13)
print('\n\tafter fromkeys: ')
print(printdic)

print('\n\tafter get: ')
print(eng2spa.get('three'))

print('\n\tafter pop: ')
print(eng2spa.pop('ten'))

eng2spa.clear()
print('\n\tafter clear: ')
print(eng2spa.keys())
print(eng2spa.values())
print(eng2spa.items())
