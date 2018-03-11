# Program 20c: Iteration of the minimal chaotic neuromodule.
# See Figure 20.13.

import matplotlib.pyplot as plt
import numpy as np

# Parameters
b1, b2, w11, w21, w12, a = -2, 3, -20, -6, 6, 1
num_iterations = 10000

def neuromodule(X):
    x,y=X
    xn=b1+w11/(1+np.exp(-a*x))+w12/(1+np.exp(-a*y))
    yn=b2+w21/(1+np.exp(-a*x))
    return xn,yn

X0 = [0, 2]
X, Y = [], []

for i in range(num_iterations):
    xn, yn = neuromodule(X0)
    X, Y = X + [xn], Y + [yn]
    X0 = [xn, yn]

fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(X, Y, color='blue', s=0.1)
plt.xlabel('x', fontsize=15)
plt.ylabel('y', fontsize=15)
plt.tick_params(labelsize=15)
plt.show()
