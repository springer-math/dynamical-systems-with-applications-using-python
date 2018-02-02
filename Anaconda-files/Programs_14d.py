# Programs 14d: Iteration of the Henon Map.
# See Figure 14.23.

import matplotlib.pyplot as plt
# Parameters
a=1.2;b=0.4;            # Set a=1 to get Figure 14.23(a).
Num_iterations=10000;

def Henon(X):
    x,y=X
    xn=1-a*x*x+y
    yn=b*x
    return xn,yn

# Ignore the first 100 iterates.
X0=[(1-b)/2,(1-b)/2]
X,Y=[],[]
for i in range(100):
    xn,yn=Henon(X0)
    X,Y=X+[xn],Y+[yn]
    X0=[xn,yn]
    
X,Y=[],[]
for i in range(Num_iterations):
    xn,yn=Henon(X0)
    X,Y=X+[xn],Y+[yn]
    X0=[xn,yn]

fig, ax = plt.subplots(figsize=(8,8))
ax.scatter(X,Y,color='blue',s=0.1)
plt.xlabel("x",fontsize=15)
plt.ylabel("y",fontsize=15)
plt.tick_params(labelsize=15)
plt.show()