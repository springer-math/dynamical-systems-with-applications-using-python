# Program 03c: Finding critical points.
# See Example 9.
import sympy as sm

x, y = sm.symbols('x, y')
P = x * (1- x / 2 - y)
Q = y * (x - 1 - y / 2)

# Set P(x,y)=0 and Q(x,y)=0.
Peqn = sm.Eq(P, 0)
Qeqn = sm.Eq(Q, 0)

# Locate critical points
criticalpoints = sm.solve((Peqn, Qeqn), x, y)

print(criticalpoints)
