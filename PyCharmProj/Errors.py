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


#ERROR 6
'''
i = [1, 2, 3, 5, 8, 13]
j = []
k = 0
for l in i:
    j[k] = l
    k += 1
print (j)
'''
#DEBUG 6: use append, an empty list does not have index
i = [1, 2, 3, 5, 8, 13]
j = []
k = 0
for l in i:
    j.append(l)
print (j)


#ERROR 7
'''
x =[1,2,3,0,0,1]
for i in range(0, len(x)):
    if x[i]==0:
        x.pop(i)
'''
#DEBUG 7: the length of the list is changed in the loop
x =[1,2,3,0,0,1]
def not0(a):
    if a != 0:
        return True
newX = filter(not0, x)
print newX


#ERROR 8
'''
my_list = [1,2,3]
[print(my_item)) for my_item in my_list]
'''
#DEBUG 8:
def func(x):
    print x
my_list = [1,2,3]

