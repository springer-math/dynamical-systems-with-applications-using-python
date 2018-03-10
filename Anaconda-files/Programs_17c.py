# Programs 17c: Barnsley's fern.
# See Figure 17.7.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# The transformation T.
f1 = lambda x,y: (0., 0.2*y)
f2 = lambda x,y: (0.85*x + 0.05*y, -0.04*x + 0.85*y + 1.6)
f3 = lambda x,y: (0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6)
f4 = lambda x,y: (-0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44)
fs = [f1, f2, f3, f4]

Num_pts = 60000

width, height = 300, 300
Fern = np.zeros((width, height))

x, y = 0, 0
for i in range(Num_pts):
    # Choose a random transformation.
    f = np.random.choice(fs, p=[0.01, 0.85, 0.07, 0.07])
    x, y = f(x,y)
    # Map (x,y) to pixel coordinates.
    # Center the image.

    cx, cy = int(width / 2 + x * width / 10), int(y * height / 10)
    Fern[cy, cx] = 1

fig, ax=plt.subplots(figsize=(8,8))
plt.imshow(Fern[::-1,:], cmap=cm.Greens)
ax.axis('off')
plt.show()
