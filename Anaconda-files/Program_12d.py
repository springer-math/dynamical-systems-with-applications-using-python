# Program 12d: The Lang-Kobayashi DDEs.
# See Figure 12.10.
# pydelay must be on your computer.

import numpy as np
import pylab as pl
from pydelay import dde23

tfinal = 10000
tau = 1000

laser_equations = {
    'E:c': '0.5*(1.0+ii*a)*E*n + K*E(t-tau)',
    'n'  : '(p - n - (1.0 +n) * pow(abs(E),2))/T'
}

params = {
    'a'  : 4.0,
    'p'  : 1.0,
    'T'  : 200.0,
    'K'  : 0.1,
    'tau': tau,
    'nu' : 10**-5,
    'n0' : 10.0
}

noise = { 'E': 'sqrt(0.5*nu*(n+n0)) * (gwn() + ii*gwn())' }

dde = dde23(eqns=laser_equations, params=params, noise=noise)
dde.set_sim_params(tfinal=tfinal)

# use a dictionary to set the history
thist = np.linspace(0, tau, tfinal)
Ehist = np.zeros(len(thist)) + 1.0
nhist = np.zeros(len(thist)) - 0.2
dic = {'t' : thist, 'E': Ehist, 'n': nhist}

# 'useend' is True by default in hist_from_dict and thus the
# time array is shifted correctly
dde.hist_from_arrays(dic)

dde.run()

t = dde.sol['t']
E = dde.sol['E']
n = dde.sol['n']

spl = dde.sample(-tau, tfinal, 0.1)

pl.plot(t[:-1], t[1:] - t[:-1], '0.8', label='step size')
pl.plot(spl['t'], abs(spl['E']), 'g', label='sampled solution')
pl.plot(t, abs(E), '.', label='calculated points')
pl.legend()

pl.xlabel('$t$')
pl.ylabel('$|E|$')

pl.xlim((0.95*tfinal, tfinal))
pl.ylim((0,3))
pl.show()
