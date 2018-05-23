# Program 05d: The Lindstedt-Poincare Method
# Deriving the order epsilon equations.
# See Example 9.

from sympy import collect, expand, Function, Symbol

x0 = Function('x0')
x1 = Function('x1')
x2 = Function('x2')
x = Function('x')
t = Symbol('t')
eps = Symbol('eps')
w1 = Symbol('w1')
w2 = Symbol('w2')

x = x0(t) + eps * x1(t) + eps ** 2 * x2(t)
expr = (1 + eps * w1 + eps ** 2 * w2) ** 2 * x.diff(t, t) + x - eps * x **3
expr = expand(expr)
expr = collect(expr, eps)

print(expr)
