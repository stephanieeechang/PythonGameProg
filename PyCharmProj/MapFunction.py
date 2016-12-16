import numpy as np
randList = list(np.random.rand(10))
print(randList)

def square(a):
   return a**2

squares = list(map(square, randList))
print(squares)
