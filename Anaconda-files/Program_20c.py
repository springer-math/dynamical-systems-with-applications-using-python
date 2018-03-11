# Programs 20c: Iteration of the minimal chaotic neuromodule.
# See Figure 20.13.

import matplotlib.pyplot as plt
import numpy as np
# Parameters
b1=-2;b2=3;w11=-20;w21=-6;w12=6;a=1;            
Num_iterations=10000;

def Neuromodule(X):
    x,y=X
    xn=b1+w11/(1+np.exp(-a*x))+w12/(1+np.exp(-a*y))
    yn=b2+w21/(1+np.exp(-a*x))
    return xn,yn

X0=[0,2]
X,Y=[],[]
for i in range(Num_iterations):
    xn,yn=Neuromodule(X0)
    X,Y=X+[xn],Y+[yn]
    X0=[xn,yn]

fig, ax = plt.subplots(figsize=(8,8))
ax.scatter(X,Y,color='blue',s=0.1)
plt.xlabel("x",fontsize=15)
plt.ylabel("y",fontsize=15)
plt.tick_params(labelsize=15)
plt.show()