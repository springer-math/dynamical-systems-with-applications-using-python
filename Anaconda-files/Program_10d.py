# Program 10d: Computing Groebner bases. See Example 6.

from sympy import groebner
from sympy.abc import x, y

g = groebner([x + y**2 - x**3, 4*x**3 - 12*x*y**2 + x**4 + 2*x**2*y**2 + y**4], order='lex')

print(g)
