# Program 13b: A second order recurrence relation.
# See Example 2.

from sympy import Function, rsolve
from sympy.abc import n

x = Function('x')
f = x(n+2) - x(n+1) - 6*x(n)
sol = rsolve(f, x(n), {x(0):1, x(1):2})

print('x_n = {}'.format(sol))
