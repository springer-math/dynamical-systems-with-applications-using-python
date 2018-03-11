# Programs 20d: Bifurcation diagram of the neuromodule.
# See Figure 20.16.
from matplotlib import pyplot as plt
import numpy as np
# Parameters
b2=3;w11=7;w21=5;w12=-4;a=1;
Max=10;start=-5;
halfN=1999;N=2*halfN+1;N1=1+halfN;
xs_up=[];xs_down=[];
x=-10;y=-3;
ns_up=np.arange(halfN)  
ns_down=np.arange(N1,N)     

# Ramp b1 up.
for n in ns_up:
    b1=start+n*Max/halfN
    x=b1+w11/(1+np.exp(-a*x))+w12/(1+np.exp(-a*y))
    y=b2+w21/(1+np.exp(-a*x))
    xn=x
    xs_up.append([n,xn])
xs_up=np.array(xs_up)  

# Ramp b1 down.
for n in ns_down:
    b1=start+2*Max-n*Max/halfN
    x=b1+w11/(1+np.exp(-a*x))+w12/(1+np.exp(-a*y))
    y=b2+w21/(1+np.exp(-a*x))
    xn=x
    xs_down.append([N-n,xn])
xs_down=np.array(xs_down)                        

fig, ax = plt.subplots()
xtick_labels = np.linspace(start, Max, 7)
ax.set_xticks([(-start+x)/Max * N1 for x in xtick_labels])
ax.set_xticklabels(['{:.1f}'.format(xtick) for xtick in xtick_labels])

plt.plot(xs_up[:,0],xs_up[:,1],'r.',markersize=0.1)
plt.plot(xs_down[:,0],xs_down[:,1],'b.',markersize=0.1)
plt.xlabel(r'$b_1$',fontsize=15)
plt.ylabel(r'$x_n$',fontsize=15)
plt.tick_params(labelsize=15)
plt.show()