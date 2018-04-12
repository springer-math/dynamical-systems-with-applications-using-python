# Program 02b: the logistic equation.
# See Example 13.
from sympy import symbols, Function, Eq, dsolve

t = symbols('t');
a = symbols('a')
b = symbols('b')
P = symbols('P', cls=Function)

sol = dsolve(Eq(P(t).diff(t), P(t) * (a-b * P(t))), P(t))

print(sol)
