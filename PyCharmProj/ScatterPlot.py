'''
Create scatter plot with a list comprehension
'''
import matplotlib.pyplot as plt
import numpy as np

t =[0.5*x-50 for x in range(200)]
points = [(x, y) for x in t for y in t if np.sqrt(x**2 + y**2) < 5]

for x, y in points:
    plt.scatter(x,y, marker='x', c='pink')

plt.show()
