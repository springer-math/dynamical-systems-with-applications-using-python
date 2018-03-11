# Programs 15a: Plot points for the Julia set.
# See Figure 15.1. 
from matplotlib import pyplot as plt
import random
from sympy import sqrt,re,im,I

# Parameters
a =0;b=1.1;          # To plot J(a,b).
k=15
Num_iterations=2**k

def Julia(X):
    x, y = X
    x1=x;y1=y;
    u = sqrt((x1-a)**2+(y1-b)**2)/2
    v=(x-a)/2
    u1=sqrt(u+v)
    v1=sqrt(u-v)
    xn=u1;yn=v1;
    if y1<b:
        yn=-yn
    if random.random() < 0.5:
        xn=-u1
        yn=-yn
    return xn, yn

x1=(re(0.5+sqrt(0.25-(a+b*I)))).expand(complex=True)
y1=(im(0.5+sqrt(0.25-(a+b*I)))).expand(complex=True)
isunstable=2*abs(x1+y1*I)
print(isunstable)

X0 = [x1, y1]
X, Y = [], []
for i in range(Num_iterations):
    xn, yn = Julia(X0)
    X, Y = X + [xn], Y + [yn]
    X0 = [xn, yn]

fig, ax = plt.subplots(figsize=(8,8))
ax.scatter(X, Y, color='blue', s=0.15)
ax.axis('off')
plt.show()