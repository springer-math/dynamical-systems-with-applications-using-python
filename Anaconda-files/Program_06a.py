# Program 06a: Contour plot. See Figure 6.2(a).

import numpy as np
import matplotlib.pyplot as plt

xlist = np.linspace(-10.0, 10.0, 100)
ylist = np.linspace(-4.0, 4.0, 100)
X, Y = np.meshgrid(xlist, ylist)
Z = Y**2 / 2 - 5*np.cos(X)

plt.figure()
plt.contour(X,Y,Z)
plt.xlabel(r'$\theta$', fontsize=20)
plt.ylabel(r'$\phi$', fontsize=20)
plt.tick_params(labelsize=20)
plt.show()
