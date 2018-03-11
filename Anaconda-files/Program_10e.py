# Program 10e: Computing Groebner bases. See Example 7.
# Reducing the first five Lyapunov quantities of a Lienard system.

from sympy import groebner, symbols

a1, a2, a3, a4, b2, b3 = symbols('a1 a2 a3 a4 b2 b3')

g = groebner([ -a1, 2*a2*b2 - 3*a3,5*b2*(2*a4 - b3*a2),
 -5*b2*(92*b2**2*a4 - 99*b3**2*a2 + 1520*a2**2*a4 - 760*a2**3*b3 - 46*b2**2*b3*a2 + 198*b3*a4),
 -b2 * (14546*b2**4*a4 + 105639*a2**3*b3**2 + 96664*a2**3*b2**2*b3 - 193328*a2**2*b2**2*a4 -
891034*a2**4*a4 + 445517*a2**5*b3 + 211632*a2*a4**2 - 317094*a2**2*b3*a4 - 44190*b2**2*b3*a4 +
22095*b2**2*b3**2*a2 - 7273*b2**4*b3*a2 + 5319*b3**3*a2 - 10638*b3**2*a4)], order='lex')

print(g)
