# Programs 10e: Computing Groebner bases. See Example 7.
# Reducing the first five Lyapunov quantities of a Lienard system.
from sympy import groebner
from sympy.abc import w,x,y,z,u,v

#Let a1=w,a2=x,a3=y,a4=z,b2=u,b3=v.
G=groebner([w,2*u*x-3*y, 5*u*(2*z-x*v),\
  -5*u*(92*z*u**2-99*x*v**2+1520*x**2*z-760*x**3*v-46*x*u**2*v+198*z*v),\
  -u*(14546*u**4*z+105639*x**3*v**2+96664*x**3*u**2*v-193328*x**2*u**2*z- \
   891034*x**4*z+445517*x**5*v+211632*x*z**2-317094*x**2*v*z- \
   44190*u**2*v*z+22095*u**2*v**2*x-7273*u**4*v*x+5319*v**3*x- \
   10638*v**2*z)],order='lex')  
            
print(G)