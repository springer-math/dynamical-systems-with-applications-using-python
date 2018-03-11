# Program 02c : Power series solution first order ODE.
# See Example 7.

from sympy import dsolve, Function, pprint
from sympy.abc import t

x = Function('x')
ODE1 = x(t).diff(t) + t * x(t) - t**3
pprint(dsolve(ODE1, hint='1st_power_series', n=8, ics={x(0): 1}))
