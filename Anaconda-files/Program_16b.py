# Program 16b: Iteration of the ikeda map.
# See Figure 16.11(b).
from matplotlib import pyplot as plt
import numpy as np

# Parameters
A, B = 10, 0.15

def ikeda(X):
    x, y = X
    xn = A + B*x*np.cos(x**2 + y**2) - B*y*np.sin(x**2 + y**2)
    yn = B*x*np.sin(x**2 + y**2) + B*y*np.cos(x**2 + y**2)
    return (xn, yn)

X0 = [A, 0]
X, Y = [], []
for i in range(10000):
    xn, yn = ikeda(X0)
    X, Y = X + [xn], Y + [yn]
    X0 = [xn, yn]

fig, ax = plt.subplots(figsize=(10,10))
ax.scatter(X, Y, color='blue', s=0.1)
plt.xlabel('$Re(E_n)$', fontsize=15)
plt.ylabel('$Im(E_n)$', fontsize=15)
plt.tick_params(labelsize=15)
plt.show()
