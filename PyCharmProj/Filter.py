import numpy as np

randList = list(np.random.rand(10))
print(randList)

def smaller05(a):
    if a < 0.5:
        return True

smallerFilter = filter(smaller05, randList)
print("Values smaller than 0.5: " + str(smallerFilter))
