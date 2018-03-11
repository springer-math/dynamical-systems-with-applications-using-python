# Programs 18e: Iterative map and power spectra.
# See Figure 18.6.

import matplotlib.pyplot as plt
from scipy.fftpack import fft
import numpy as np

# Parameters
a=1;b=0.3;              # To get Figures 18.6(e) and (f).
N=50000;

def Map2D(X):
    x,y=X
    xn=1-a*y**2+b*x
    yn=x
    return xn,yn

X0=[(1-b)/2,(1-b)/2]
X,Y=[],[]
for i in range(N):
    xn,yn=Map2D(X0)
    X,Y=X+[xn],Y+[yn]
    X0=[xn,yn]

fig, ax = plt.subplots(figsize=(8,8))
ax.scatter(X,Y,color='blue',s=0.05)
plt.xlabel("x",fontsize=15)
plt.ylabel("y",fontsize=15)
plt.tick_params(labelsize=15)

fig2 = plt.figure()
f=np.linspace(-1,1,N)
Pow=np.abs(fft(X)**2)
Pow=np.log(Pow)
plt.plot(f,Pow)
plt.xlim(0,1)
plt.xlabel("Frequency (Hz)",fontsize=15)
plt.ylabel("log(Power)",fontsize=15)
plt.tick_params(labelsize=15)
plt.show()
