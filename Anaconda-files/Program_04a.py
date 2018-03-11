# Program 04a: Holling-Tanner model. See Figures 4.5 and 4.6.
# Time series and phase portrait for a predator-prey system.
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

# The Holling-Tanner model.
def holling_tanner(X, t=0):
    # here X[0] = x and X[1] = y
    return np.array([X[0] * (1 - X[0]/7) - 6 * X[0] * X[1] / (7 + 7*X[0]),
                    0.2 * X[1] * (1 - 0.5 * X[1] / X[0])])

t = np.linspace(0, 200, 1000)
# initial values: x0 = 7, y0 = 0.1
Sys0 = np.array([7, 0.1])

X, infodict = integrate.odeint(holling_tanner, Sys0, t, full_output=True)
x, y = X.T

fig = plt.figure(figsize=(15, 5))
fig.subplots_adjust(wspace=0.5, hspace=0.3)
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

ax1.plot(t,x, 'r-', label='prey')
ax1.plot(t,y, 'b-', label='predator')
ax1.set_title('Time Series')

ax1.set_xlabel('time')
ax1.grid()
ax1.legend(loc='best')

ax2.plot(x, y, color='blue')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('Phase portrait')
ax2.grid()

plt.show()
