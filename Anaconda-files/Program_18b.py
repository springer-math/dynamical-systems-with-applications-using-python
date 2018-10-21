# Programs 18d: Counting white pixels in color picture of a raccoon.
# See Figure 18.2.

from scipy import misc
import matplotlib.pyplot as plt
import numpy as np

face = misc.face()

fig1 = plt.figure()
plt.imshow(face)
height, width, _ = face.shape

print('Image dimensions: {}x{}'.format(width, height))

white_pixels = np.all(face > 180, axis=2)

fig2 = plt.figure()
plt.imshow(white_pixels, cmap='gray')
print('There are {:,} white pixels'.format(int(np.sum(white_pixels))))
plt.show()
