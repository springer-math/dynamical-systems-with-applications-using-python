# Programs 21e: Pinched hysteresis in a memristor.
# See Figure 21.12.

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constants
eta=1.0;L=1.0;Roff=70.0;Ron=1.0;p=10.0;T=20.0;w0=0.5;       

t=np.arange(0.0, 40.0, 0.01)

# Set up the ODEs, see equations (21.3).
def Memristor(X,t):
    w=X
    dwdt=(eta*(1-(2*w-1)**(2*p))*np.sin(2*np.pi*t/T))/(Roff-(Roff-Ron)*w)
    return dwdt
    
X = odeint(Memristor, [w0], t, rtol=1e-12)
w = X[:,0]

plt.plot(np.sin(2*np.pi*t/T),np.sin(2*np.pi*t/T)/(Roff-(Roff-Ron)* \
                X[:,0]),'b')
plt.xlabel('voltage',fontsize=15)
plt.ylabel('current',fontsize=15)
plt.tick_params(labelsize=15)
plt.show()