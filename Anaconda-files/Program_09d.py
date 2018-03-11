# Programs 9d: Bifurcation diagram of the Duffing equation.
# See Figure 9.14.

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

k=0.3;omega=1.25;alpha=1;beta=-1;
rs_up=[];rs_down=[];
def Duffing(x, t):
    return [x[1],-beta*x[0]-k*x[1]-alpha*x[0]**3+  \
            Gamma*np.cos(omega*t)]
    
# Take N_steps=4000 to get Figure 9.13.
N_steps=4002;step=0.0001;interval=N_steps*step;a=1;b=0;
ns=np.linspace(0,N_steps,N_steps)

# Ramp the amplitude of vibration, Gamma, up.
for n in ns:
    Gamma=step*n
    t=np.linspace(0,(4*np.pi)/omega,200)
    xs=odeint(Duffing,[a,b],t)
    for i in range(2):
        a=xs[100,0]
        b=xs[100,1]
        r=np.sqrt(a**2+b**2)
        rs_up.append([n,r])
    
rs_up=np.array(rs_up) 

# Ramp the amplitude of vibration, Gamma, down.
for n in ns:
    Gamma=interval-step*n
    t=np.linspace(0,(4*np.pi)/omega,200)
    xs=odeint(Duffing,[a,b],t)
    for i in range(2):
        a=xs[100,0]
        b=xs[100,1]
        r=np.sqrt(a**2+b**2)
        rs_down.append([N_steps-n,r])
    
rs_down=np.array(rs_down)

fig, ax = plt.subplots()
xtick_labels = np.linspace(0, interval, 5)
ax.set_xticks([x / interval * N_steps for x in xtick_labels])
ax.set_xticklabels(['{:.1f}'.format(xtick) for \
                    xtick in xtick_labels])

plt.plot(rs_up[:,0],rs_up[:,1],'r.',markersize=0.1)
plt.plot(rs_down[:,0],rs_down[:,1],'b.',markersize=0.1)
plt.xlabel(r'$\Gamma$',fontsize=15)
plt.ylabel("r",fontsize=15)
plt.tick_params(labelsize=15)
plt.show()
