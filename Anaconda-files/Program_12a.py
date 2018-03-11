# Program 12a: The method of steps.
# See Figure 12.1.

from sympy import integrate,symbols

xi, t, i = symbols('xi t i')

def phi(i, t):
    if i == 0:
        return 1  # Initial history x(t)=1 on [-1,0]
    else:
        return phi(i-1, i-1) - integrate(phi(i-1, xi-1), (xi, i-1, t))

tmax = 10
x = [phi(j, t) for j in range(tmax + 1)]

print('x(t) = {}'.format(x))
