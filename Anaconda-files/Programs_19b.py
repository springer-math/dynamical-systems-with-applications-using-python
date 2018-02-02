# Programs 19b: Chaos control in the Henon Map.
# See Figure 19.6.

import matplotlib.pyplot as plt
import numpy as np
# Parameters
a=1.2;b=0.4;   
xstar=0.8358;ystar=xstar; 
k1=-1.8;k2=1.2;        
N_iter=199;
rs=[];x=0.5;y=0.6;
ns=np.arange(N_iter)
nsc=np.arange(N_iter,2*N_iter)

for n in ns:
    xn=a+b*y-x**2
    yn=x
    x=xn;y=yn;
    r=np.sqrt(x**2+y**2)
    rs.append([n,r])

# Check point is in control region.    
print(x,y)

for n in nsc:
    xn=-k1*(x-xstar)-k2*(y-ystar)+a+b*y-x**2
    yn=x
    x=xn;y=yn;
    r=np.sqrt(x**2+y**2)
    rs.append([n,r])

rs=np.array(rs)

fig, ax = plt.subplots(figsize=(8,8))
plt.plot(rs[:,0],rs[:,1])
plt.plot(rs[:,0],rs[:,1],'ro')
plt.xlabel("n",fontsize=15)
plt.ylabel(r"$r_n^2$",fontsize=15)
plt.tick_params(labelsize=15)
plt.show()