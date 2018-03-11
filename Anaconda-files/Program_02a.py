# Program 2a: A separabale ODE.
from sympy import symbols, Function, Eq, dsolve

t = symbols('t')
x = symbols('x', cls=Function)
sol = dsolve(Eq(x(t).diff(t), -t/x(t)), x(t))

print(sol)
