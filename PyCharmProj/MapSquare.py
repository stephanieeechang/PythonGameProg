def square(a):
    sqr = a**2
    return sqr

inputs = range(10) # start with list [0,1,2,3,4,5,6,7,8]
squares = []  # An empty list for the results
for x in inputs: # step over every element in the list
    squares.append(square(x)) # grow the list one element at a time
for i in squares:
    print(i)
