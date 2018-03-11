# Program 15c: The Mandelbrot set.
# See Figure 15.3.

import numpy as np
import matplotlib.pyplot as plt

xmin, xmax = -2.5, 1
ymin, ymax = -1.5, 1.5
xrange, yrange = xmax-xmin, ymax-ymin

def mandelbrot(h,w, max_iter=50):
     y, x = np.ogrid[ymin:ymax:h*1j, xmin:xmax:w*1j]
     c = x + y*1j
     z = c
     div_iter = max_iter + np.zeros(z.shape, dtype=int)

     for i in range(max_iter):
         z = z**2 + c
         div_test = z*np.conj(z) > 2**2
         div_num = div_test & (div_iter == max_iter)
         div_iter[div_num] = i
         z[div_test] = 2

     return div_iter  # Number of iterations to diverge

scale = 1000  # Amount of detail in the set

# Set the tick labels to the Argand plane
fig, ax = plt.subplots()
ax.imshow(mandelbrot(scale,scale))
xtick_labels = np.linspace(xmin, xmax, xrange / 0.5)
ax.set_xticks([(x-xmin) / xrange * scale for x in xtick_labels])
ax.set_xticklabels(['{:.1f}'.format(xtick) for xtick in xtick_labels])
ytick_labels = np.linspace(ymin, ymax, yrange / 0.5)
ax.set_yticks([-(y+ymin) / yrange * scale for y in ytick_labels])
ax.set_yticklabels(['{:.1f}'.format(ytick) for ytick in ytick_labels])
plt.show()
