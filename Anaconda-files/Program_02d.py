# Program 02d : Power series solution of second order ODE.
# See Example 8.
from sympy import dsolve, Function, pprint
from sympy.abc import t

x = Function('x')
ODE2 = x(t).diff(t, 2) + t**2*x(t).diff(t) - x(t)

pprint(dsolve(ODE2, hint='2nd_power_series_ordinary', n=6))
