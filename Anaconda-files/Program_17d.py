# Program 17d: Plot tau curve, D_q curve and f(alpha) curve.
# See Figure 17.16.

import numpy as np
import matplotlib.pyplot as plt
import scipy.misc

plt.subplots_adjust(hspace=1)
plt.figure(1)

# The tau curve
x = np.linspace(-20, 20, 1000)
y = (np.log((1/9)**x + (8/9)**x) / np.log(3))

plt.subplot(3, 1, 1)
plt.plot(x, y)
plt.xlabel('$q$', fontsize=15)
plt.ylabel(r'$\tau(q)$', fontsize=15)
plt.tick_params(labelsize=15)

# The D_q curve
x1 = np.linspace(-20, 0.99, 100)
x2 = np.linspace(0.99, 20, 100)
Dq1 = (np.log((1/9)**x1 + (8/9)**x1) / (np.log(3) * (1 - x1)))
Dq2 = (np.log((1/9)**x2 + (8/9)**x2) / (np.log(3) * (1 - x2)))
plt.subplot(3, 1, 2)
plt.plot(x1, Dq1, x2, Dq2)
plt.xlabel('q', fontsize=15)
plt.ylabel('$D_q$', fontsize=15)
plt.tick_params(labelsize=15)

# The f(alpha) curve
p1, p2 = 1/9, 8/9
k = 500
s = np.arange(500)
x = (s*np.log(p1) + (k-s) * np.log(p2)) / (k*np.log(1/3))
f = -(np.log(scipy.misc.comb(k, s))) / (k*np.log(1/3))

plt.subplot(3, 1, 3)
plt.plot(x, f)
plt.xlabel(r'$\alpha$', fontsize=15)
plt.ylabel(r'$f(\alpha)$', fontsize=15)
plt.tick_params(labelsize=15)
plt.show()
