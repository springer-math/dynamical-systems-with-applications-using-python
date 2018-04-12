# Program 15b: Colormap of a Julia set.
# See Figure 15.2.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm  # Use a colormap

# Set image dimensions
im_w, im_h = 500, 500
c = complex(-0.1, 0.65)  # To plot J(a,b)
max_abs_z = 10
max_iter = 1000
xmin, xmax = -2, 2
xrange = xmax - xmin
ymin, ymax = -2, 2
yrange = ymax - ymin

julia = np.zeros((im_w, im_h))
for re_z in range(im_w):
    for im_y in range(im_h):
        nit = 0
        # Map pixel position to a point in the plane
        z = complex(re_z / im_w * xrange + xmin,
                    im_y / im_h * yrange + ymin)
        # Do the iterations
        while abs(z) <= max_abs_z and nit < max_iter:
            z = z**2 + c
            nit += 1
        ratio = nit / max_iter
        julia[-im_y, re_z] = ratio  # Set axes to Re(z) and Im(z)

fig, ax = plt.subplots()
ax.axis('off')
ax.imshow(julia, interpolation='nearest', cmap=cm.hot)
plt.show()
