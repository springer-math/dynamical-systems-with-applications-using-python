# Program 19a: Chaos control in the logistic map.
# Control to period two.
# See Figure 19.3(b).

import matplotlib.pyplot as plt
import numpy as np

# Parameters
mu = 4
k = 0.217
num_iterations = 60
xs, x = [], [0.6]
ns = np.arange(0, num_iterations, 2)
nsc = np.arange(num_iterations, 2*num_iterations, 2)

for n in ns:
    x1 = mu*x[n] * (1 - x[n])
    x.append(x1)
    xs.append([n, x1])
    x2 = mu*x1 * (1 - x1)
    x.append(x2)
    xs.append([n+1, x2])

for n in nsc:
    x1 = k*mu*x[n] * (1 - x[n])
    x.append(x1)
    xs.append([n, x1])
    x2 = mu*x1 * (1 - x1)
    x.append(x2)
    xs.append([n+1, x2])

xs = np.array(xs)

fig, ax = plt.subplots(figsize=(8, 8))
plt.plot(xs[:, 0], xs[:, 1])
plt.plot(xs[:, 0], xs[:, 1], 'ro')
plt.xlabel('n', fontsize=15)
plt.ylabel(r'$x_n$', fontsize=15)
plt.tick_params(labelsize=15)
plt.show()
