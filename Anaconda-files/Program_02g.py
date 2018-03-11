# Program 02g: A second order ODE.
from sympy import symbols, dsolve, Function, Eq, sin

t = symbols('t')
I = symbols('I', cls=Function)
sol = dsolve(Eq(I(t).diff(t,t) + 5*I(t).diff(t) + 6*I(t), 10*sin(t)), I(t))

print(sol)
