# Program 02f: A linear first order ODE.
from sympy import Function, dsolve, Eq, symbols, sin

t = symbols('t');
I = symbols('I', cls=Function)
sol = dsolve(Eq(I(t).diff(t), 5*sin(t) - I(t)/5), I(t))

print(sol)
