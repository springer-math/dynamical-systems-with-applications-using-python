# Program 10b: Polynomial Reduce. See Example 4.

from sympy import reduced
from sympy.abc import x, y, z

f = x**4 + y**4 + z**4

p = reduced(f, [x**2+y, z**2*y-1, y-z**2])
print(p)

q = reduced(f, [y - z**2, z**2 * y - 1, x**2 + y])
print(q)
