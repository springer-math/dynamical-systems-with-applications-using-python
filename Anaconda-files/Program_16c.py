# Programs 16c: Bifurcation diagram of the Ikeda map.
# See Figure 16.16(d).

from matplotlib import pyplot as plt
import numpy as np

# Parameters
C = 0.345913
kappa = 0.0225
Pmax = 120
phi = np.pi
half_N = 1999
N = 2*half_N + 1
N1 = 1 + half_N
esqr_up, esqr_down = [], []
E1 = E2 = 0
ns_up = np.arange(half_N)
ns_down = np.arange(N1, N)

# Ramp the power up
for n in ns_up:
    E2 = E1 * np.exp(1j*((abs(C*E1))**2 - phi))
    E1 = 1j * np.sqrt(1 - kappa) * np.sqrt(n * Pmax / N1) + np.sqrt(kappa) * E2
    esqr1 = abs(E1)**2
    esqr_up.append([n, esqr1])

esqr_up = np.array(esqr_up)

# Ramp the power down
for n in ns_down:
    E2 = E1 * np.exp(1j * ((abs(C*E1))**2 - phi))
    E1 = 1j * np.sqrt(1 - kappa) * np.sqrt(2 * Pmax - n * Pmax / N1) + np.sqrt(kappa) * E2
    esqr1 = abs(E1)**2
    esqr_down.append([N-n, esqr1])

esqr_down=np.array(esqr_down)

fig, ax = plt.subplots()
xtick_labels = np.linspace(0, Pmax, 6)
ax.set_xticks([x / Pmax * N1 for x in xtick_labels])
ax.set_xticklabels(['{:.1f}'.format(xtick) for xtick in xtick_labels])

plt.plot(esqr_up[:, 0], esqr_up[:, 1], 'r.', markersize=0.1)
plt.plot(esqr_down[:, 0], esqr_down[:, 1], 'b.', markersize=0.1)
plt.xlabel('Input', fontsize=15)
plt.ylabel('Output', fontsize=15)
plt.tick_params(labelsize=15)
plt.show()
