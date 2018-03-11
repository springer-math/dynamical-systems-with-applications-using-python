# Program 12b: Solution of a DDE using the method of steps.
# See Figure 12.1. The plot is a piecewise function.
# The lambda t: functions are computed in Programs 12a.

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-1, 10, 1000)

conditions = [t<=0, t>0, t>1, t>2, t>3, t>4, t>5, t>6, t>7, t>8, t>9]

lambdas = [
    lambda t: 1,
    lambda t: 1-t,
    lambda t: t**2 / 2 - 2*t + 3/2,
    lambda t: -t**3 / 6 + 3*t**2 / 2 - 4*t + 17/6,
    lambda t: t**4 / 24 - 2*t**3 / 3 + 15*t**2 / 4 - 17*t / 2 + 149/24,
    lambda t: -t**5 / 120 + 5*t**4 / 24 - 2*t**3 + 109*t**2/12 - 115*t / 6 + 1769/120,
    lambda t: t**6 / 720 - t**5 / 20 + 35*t**4 / 48 - 197*t**3 / 36 + 1061*t**2 / 48 - 1085*t / 24 + 26239/720,
    lambda t: -t**7 / 5040 + 7*t**6 / 720 - t**5 / 5 + 107*t**4 / 48 - 521*t**3 / 36 + 13081*t**2 / 240 - 13201*t / 120 + 463609/5040,
    lambda t: t**8 / 40320 - t**7 / 630 + 7*t**6 / 160 - 487*t**5 / 720 + 3685*t**4 / 576 - 27227*t**3 / 720 + 39227*t**2 / 288 - 39371*t / 144 + 3157891/13440,
    lambda t: -t**9 / 362880 + t**8 / 4480 - t**7 / 126 + 701*t**6 / 4320 - 1511*t**5 / 720 + 51193*t**4 / 2880 - 212753*t**3 / 2160 + 1156699*t**2 / 3360 - 1158379*t / 1680 + 43896157/72576,
    lambda t: t**10 / 3628800 - t**9 / 36288 + 11*t**8 / 8960 - 323*t**7 / 10080 + 1873*t**6 / 3456 - 89269*t**5 / 14400 + 279533*t**4 / 5760 - 7761511*t**3 / 30240 + 23602499*t**2 / 26880 - 23615939*t / 13440 + 5681592251/3628800
]

plt.plot(t, np.piecewise(t, conditions, lambdas))

plt.xlabel('t', fontsize=25)
plt.ylabel('x(t)', fontsize=25)
plt.tick_params(labelsize=25)
plt.show()
