# Programs 14a: Graphical iteration of the tent map.
# See Figure 14.7(a).

from sympy import Rational
import numpy as np
import matplotlib.pyplot as plt

x = Rational(1, 5)  # Initial value
inputs = np.array([x])
outputs = np.array([0])
print(x)

for i in range(2, 10):
    inputs = np.append(inputs, x)
    inputs = np.append(inputs, x)
    outputs = np.append(outputs, x)
    if x < Rational(1, 2):
        x = 2 * x
    elif x > Rational(1, 2):
        x = 2 - 2 * x
    outputs = np.append(outputs, x)
    print(x)

plt.plot(inputs, outputs, lw=2)

# Plot the tent function and line y=x.
X1 = np.linspace(0, 0.5, 100, endpoint=True)
X2 = np.linspace(0.5, 1, 100, endpoint=True)
X = np.linspace(0, 1, 200, endpoint=True)
plt.plot(X1, 2*X1, 'k-')
plt.plot(X2, 2*(1-X2), 'k-')
plt.plot(X, X, 'r-')
plt.xlabel('x', fontsize=15)
plt.ylabel('T(x)', fontsize=15)
plt.tick_params(labelsize=15)

plt.show()
