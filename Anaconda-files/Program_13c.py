# Program 13c: The Leslie matrix. See Example 4.
# Compute the population distribution after 50 years.
# Determine the eigenvalues and eigenvectors of a Leslie matrix.

import numpy as np
import numpy.linalg as LA

L = np.array([[0,3,1], [0.3,0,0], [0,0.5,0]])
X0 = np.array([[1000], [2000], [3000]])
X_50 = np.dot(LA.matrix_power(L, 50), X0)
X_50 = X_50.round()
print('X(50) = {}'.format(X_50))

dL, VL = LA.eig(L)
print('Eigenvalues = {}'.format(dL))
print('Eigenvectors = {}'.format(VL))
