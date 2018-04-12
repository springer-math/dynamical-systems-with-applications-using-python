# Programs 18d: Counting white pixels in color picture of a raccoon.
# See Figure 18.2.

from scipy import misc
import matplotlib.pyplot as plt
import numpy as np

face = misc.face()

fig1 = plt.figure()
plt.imshow(face)
width, height, _ = face.shape

print('Image dimensions: {}x{}'.format(width, height))
white_pixels = np.zeros((width, height))

def white_pixel_filter(pixel, threshold):
    return 1 if all(value > threshold for value in pixel) else 0

for i, row in enumerate(face):
    for j, pixel in enumerate(row):
        white_pixels[i, j] = white_pixel_filter(pixel, threshold=180)

fig2 = plt.figure()
plt.imshow(white_pixels, cmap='gray')
print('There are {:,} white pixels'.format(int(np.sum(white_pixels))))
plt.show()
