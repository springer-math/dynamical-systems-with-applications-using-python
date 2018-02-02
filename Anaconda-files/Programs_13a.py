# Programs_13a
from sympy import Function, rsolve
from sympy.abc import n
x=Function('x');
f=x(n+1)-(1+3/100)*x(n);
sol=rsolve(f,x(n),{x(0):10000});
print('x_n=',sol)
x_5=round(sol.subs(n,5),2)
print('x(5)=£',x_5)