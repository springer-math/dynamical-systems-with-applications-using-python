# Program 15a: Plot points for the julia set.
# See Figure 15.1.

from matplotlib import pyplot as plt
from random import random
from sympy import sqrt, re, im, I

# Parameters
a,b = 0, 1.1  # To plot J(a,b).
k = 15
num_iterations = 2**k

def julia(X):
    x, y = X
    x1, y1 = x, y
    u = sqrt((x1-a)**2 + (y1-b)**2) / 2
    v = (x - a) / 2
    u1, v1 = sqrt(u + v), sqrt(u - v)
    xn, yn = u1, v1
    if y1 < b:
        yn = -yn
    if random() < 0.5:
        xn, yn = -u1, -yn
    return (xn, yn)

x1 = (re(0.5 + sqrt(0.25 - (a + b*I)))).expand(complex=True)
y1 = (im(0.5 + sqrt(0.25 - (a + b*I)))).expand(complex=True)
is_unstable = 2 * abs(x1 + y1*I)
print(is_unstable)

X0 = [x1, y1]
X, Y = [], []
for i in range(num_iterations):
    xn, yn = julia(X0)
    X, Y = X + [xn], Y + [yn]
    X0 = [xn, yn]

fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(X, Y, color='blue', s=0.15)
ax.axis('off')
plt.show()
