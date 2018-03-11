# Programs 20b: The discrete Hopfield network.
# See Example 5.

from sympy import Matrix, eye
import random

# The fundamental memories:
x1 = [1, 1, 1, 1, 1]
x2 = [1, -1, -1, 1, -1]
x3 = [-1, 1, -1, 1, 1]

X = Matrix([x1, x2, x3])
W = X.T * X / 5 - 3*eye(5) / 5

def hsgn(v, x):
    if v > 0:
        return 1
    elif v == 0:
        return x
    else:
        return -1

L = [0, 1, 2, 3, 4]
n = random.sample(L, len(L))

xinput = [1, -1, -1, 1, 1]
xtest = xinput
for j in range(4):
    M = W.row(n[j]) * Matrix(xtest)
    xtest[n[j]] = hsgn(M[0], xtest[n[j]])

if xtest == x1:
    print('Net has converged to X1')
elif xtest == x2:
    print('Net has converged to X2')
elif xtest == x3:
    print('Net has converged to X3')
else:
    print('Iterate again: May have converged to spurious state')
