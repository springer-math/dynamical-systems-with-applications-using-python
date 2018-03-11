# Program 10c: The S-Polynomial. See Example 5.
from sympy import expand, LM, LT, lcm
from sympy.abc import x, y, z

def s_polynomial(f, g):
    return expand(lcm(LM(f), LM(g))*(1/LT(f)*f - 1/LT(g)*g))

f, g = [x - 13*y**2 - 12*z**3, x**2 - x*y + 92*z]
s = s_polynomial(f, g)

print(s)
