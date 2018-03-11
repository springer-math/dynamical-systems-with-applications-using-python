# Programs 14c: Lyapunov exponents of the logistic map.
# See Figure 14.17.
import numpy as np
import matplotlib.pyplot as plt

Numpoints=16000;
result = []
lambdas = []
maps = []
xmin = 3
xmax = 4
mult=(xmax-xmin)*Numpoints

muvalues = np.arange(xmin, xmax, 20/Numpoints)

for r in muvalues:
    x = 0.1
    result = []
    for t in range(100):
        x = r * x * (1 - x)
        result.append(np.log(abs(r - 2*r*x)))
    lambdas.append(np.mean(result))
    # Ignore first 100 iterates.
    for t in range(20):
        x = r * x * (1 - x)
        maps.append(x)    
    
fig = plt.figure(figsize=(10,7))
ax1 = fig.add_subplot(1,1,1)

xticks = np.linspace(xmin, xmax, mult)
zero = [0]*mult
ax1.plot(xticks,zero,'k-',linewidth=3)
ax1.plot(xticks, maps,'r.',alpha = 0.3,label='Logistic map')
ax1.set_xlabel('r')
ax1.plot(muvalues,lambdas,'b-',linewidth= 1,label='Lyapunov exponent')
ax1.grid('on')
ax1.set_ylim(-1, 1)
ax1.set_xlabel('$\mu$',fontsize=15)
ax1.legend(loc='best')
ax1.set_title('Logistic map versus Lyapunov exponent',fontsize=15)