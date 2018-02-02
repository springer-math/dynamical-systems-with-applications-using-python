# Programs 15b: Colormap of a Julia set.
# See Figure 15.2.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm          # Use a colormap.

# Set image dimensions.
Im_w, Im_h = 500, 500
c = complex(-0.1,0.65)            # To plot J(a,b).
Max_abs_z = 10
Max_iter = 1000
xmin, xmax = -2, 2
xrange = xmax - xmin
ymin, ymax = -2, 2
yrange = ymax - ymin

Julia = np.zeros((Im_w, Im_h))
for Re_z in range(Im_w):
    for Im_y in range(Im_h):
        nit = 0
        # Map pixel position to a point in the plane
        z = complex(Re_z / Im_w * xrange+ xmin,
                    Im_y / Im_h * yrange + ymin)
        # Do the iterations
        while abs(z) <= Max_abs_z and nit < Max_iter:
            z = z**2 + c
            nit += 1
        ratio = nit / Max_iter
        Julia[-Im_y,Re_z] = ratio     # Set axes to Re(z) and Im(z).

fig, ax = plt.subplots()
ax.axis('off')
ax.imshow(Julia, interpolation='nearest', cmap=cm.hot)
plt.show()