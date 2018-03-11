# Program 14d: Iteration of the Henon Map.
# See Figure 14.23.

import matplotlib.pyplot as plt

# Parameters
a = 1.2  # Set a=1 to get Figure 14.23(a)
b = 0.4
num_iterations = 10000

def henon(X):
    x,y=X
    xn=1-a*x*x+y
    yn=b*x
    return xn,yn

# Ignore the first 100 iterates
X0 = [(1 - b) / 2, (1 - b) / 2]
X, Y = [], []
for i in range(100):
    xn, yn = henon(X0)
    X, Y = X + [xn], Y + [yn]
    X0 = [xn, yn]

X, Y = [], []
for i in range(num_iterations):
    xn, yn = henon(X0)
    X, Y = X + [xn], Y + [yn]
    X0 = [xn, yn]

fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(X, Y, color='blue', s=0.1)
plt.xlabel('x', fontsize=15)
plt.ylabel('y', fontsize=15)
plt.tick_params(labelsize=15)
plt.show()
