# Program 01d: Subplots.
# See Figure 1.15.

import matplotlib.pyplot as plt
import numpy as np

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)  # subplot(num rows, num cols, fig num)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k', label='damping')
plt.xlabel('time (s)')
plt.ylabel('amplitude (m)')
plt.title('Damped pendulum')
legend = plt.legend(loc='upper center', shadow=True)

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'g--', linewidth=4)
plt.xlabel('time (s)')
plt.ylabel('amplitude (m)')
plt.title('Undamped pendulum')
plt.subplots_adjust(hspace=0.8)

plt.show()
