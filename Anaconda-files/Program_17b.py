# Program 17b: The chaos game and Sierpinski triangle.
# See Figure 17.6.

import matplotlib.pyplot as plt
from random import random, randint
import numpy as np

def midpoint(P, Q):
    return (0.5*(P[0] + Q[0]), 0.5*(P[1] + Q[1]))

# The three vertices.
vertices = [(0, 0), (2, 2*np.sqrt(3)), (4, 0)]

iterates = 50000
x, y = [0]*iterates, [0]*iterates
x[0], y[0] = random(), random()

for i in range(1, iterates):
    k = randint(0, 2)
    x[i], y[i] = midpoint(vertices[k], (x[i-1], y[i-1]))

fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(x, y, color='r', s=0.1)
ax.axis('off')
plt.show()
