# Program 02a: A separabale ODE.
# See Example 1.

from sympy import symbols, Function, Eq, dsolve

t = symbols('t')
x = symbols('x', cls=Function)
sol = dsolve(Eq(x(t).diff(t), -t/x(t)), x(t))

print(sol)
