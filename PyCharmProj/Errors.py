'''
fix the errors
'''

#ERROR 1
#numbers = ('Bob':'322', 'Mary':'110', 'Joe':'839')
#DEBUG 1: use {} instead of ()
numbers = {'Bob':'322', 'Mary':'110', 'Joe':'839'}


#ERROR 2
'''
mydict = ('a':'1', 'b':'2')
mydict['a']
mydict['c']
'''
#DEBUG 2: use {} instead of (), use get()
mydict = {'a':'1', 'b':'2'}
mydict['a']
print mydict.get('c','Invalid key!')


#ERROR 3
'''
d = {}
d.update([(1,)])
'''
#DEBUG 3: should put dictionary in update() instead of a list
d = {}
d.update({1:2})
print d


#ERROR 4
'''
mapping = {1:22.5, 8:13.4, 10:12.1}
average = [sum(v)/len(v) for k,v in mapping.items()]
'''
#DEBUG 4: should not use a list comprehension, since the for loop is returning one value at a time
mapping = {1:22.5, 8:13.4, 10:12.1}
sum = 0
for v in mapping.values():
    sum += v
average = sum/len(mapping)
print average

print "hello"
#ERROR 5
b = {'video':0, 'music':23}
k = b.keys()
print type(k)
print k[0]

"""
print k
#DEBUG 5:
b = {'video':0, 'music':23}
k = list(b.keys())
print k[0]
print k
"""
