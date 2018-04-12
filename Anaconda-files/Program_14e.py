# Program 14e: Lyapunov quantities of the Henon map.
# See Exercise 8(c).

import numpy as np

a = 1.2
b = 0.4
x = y = 0
vec1 = [1, 0]
vec2 = [0, 1]

for i in range(490):
     xn = 1 - a*x*x + y
     yn = b*x
     x = xn
     y = yn
     J = np.array([[-2*a*x, 1], [b, 0]])
     vec1 = J.dot(vec1)
     vec2 = J.dot(vec2)
     dotprod1 = np.dot(vec1, vec1)
     dotprod2 = np.dot(vec1, vec2)
     vec2 = vec2 - np.multiply((dotprod2 / dotprod1), vec1)
     lengthv1 = np.sqrt(dotprod1)
     area = np.multiply(vec1[0], vec2[1]) - np.multiply(vec1[1], vec2[0])
     h1 = np.log(lengthv1) / i
     h2 = np.log(area) / i - h1

print('h_1 = {}'.format(h1))
print('h_2 = {}'.format(h2))
