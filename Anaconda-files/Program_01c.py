# Program 01c: Two curves on one plot.
# See Figure 1.14.

import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.01)
c = 1 + np.cos(2*np.pi*t)
s = 1 + np.sin(2*np.pi*t)

plt.plot(t, s, 'r--', t, c, 'b-.')
plt.xlabel('time (s)')
plt.ylabel('voltage (mV)')
plt.title('Voltage-time plot')
plt.grid(True)
plt.savefig('Voltage-Time Plot.png')
plt.show()
