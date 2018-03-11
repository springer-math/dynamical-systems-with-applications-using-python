# Programs 20a: The generalized delta learning rule.
# See figure 20.7.

import matplotlib.pyplot as plt
import numpy as np

data=np.loadtxt("housing.txt")

numdatas=4         # Using 4 columns from data in this case.
numPatterns=506;
X=data[:,[5,8,12]]
t=data[:,13]
ws1=[];ws2=[];ws3=[];ws4=[];k=0;

xmean=X.mean(axis=0)
xstd=X.std(axis=0)
X=(X-xmean*np.array([np.ones(numPatterns)]).T) \
  /(xstd*np.array([np.ones(numPatterns)]).T)
X=np.c_[np.ones(numPatterns),X]

tmean=(max(t)+min(t))/2
tstd=(max(t)-min(t))/2
t=(t-tmean)/tstd

w=0.1*np.random.random(numdatas)
y1=np.tanh(X.dot(w))
e1=t-y1
mse=np.var(e1)

# Do numEpochs iterations.
numEpochs=10;numPatterns=506;
eta=0.001;k=1;
for m in range(numEpochs):
    for n in range(numPatterns):
        yk=np.tanh(X[n,:].dot(w))
        err=yk-t[n]
        g=X[n,:].T*((1-yk**2)*err)
        w=w-eta*g
        k=k+1
        ws1.append([k,np.array(w[0]).tolist()])
        ws2.append([k,np.array(w[1]).tolist()])
        ws3.append([k,np.array(w[2]).tolist()])
        ws4.append([k,np.array(w[3]).tolist()])


ws1=np.array(ws1);ws2=np.array(ws2);
ws3=np.array(ws3);ws4=np.array(ws4)
plt.plot(ws1[:,0],ws1[:,1],'k.',markersize=0.1)
plt.plot(ws2[:,0],ws2[:,1],'g.',markersize=0.1)
plt.plot(ws3[:,0],ws3[:,1],'b.',markersize=0.1)
plt.plot(ws4[:,0],ws4[:,1],'r.',markersize=0.1)
plt.xlabel("Number of iterations",fontsize=15)
plt.ylabel("Weights",fontsize=15)
plt.tick_params(labelsize=15)
plt.show()
