# Program 01b: A program that solves a second order ODE.

from sympy import Function, Eq, dsolve, symbols, exp

t = symbols('t')
y = symbols('y', cls=Function)

deqn2 = Eq(y(t).diff(t, t) + y(t).diff(t) + y(t), exp(t))
sol2 = dsolve(deqn2, y(t))

print(sol2)
