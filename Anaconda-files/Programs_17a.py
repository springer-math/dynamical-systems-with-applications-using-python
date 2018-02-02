# Programs 17a: Plotting the Koch curve.
# See Figure 17.2.

import numpy as np
import matplotlib.pyplot as plt
from math import floor

k=6;N_lines=4**k;h=3**(-k);
x = [0]*(N_lines+1)
y = [0]*(N_lines+1)
x[0] = 0
y[0] = 0
                                        
segment=[0]*N_lines;
        
# The angles of the four segments. 
angle=[0,np.pi/3,-np.pi/3,0]   
for i in range(N_lines):
    m=i;ang=0;
    for j in range(k):
        segment[j]=np.mod(m,4)
        m=floor(m/4)
        ang=ang+angle[segment[j]]
        
    x[i+1]=x[i]+h*np.cos(ang)
    y[i+1]=y[i]+h*np.sin(ang)

plt.axis('equal')
plt.plot(x,y)  