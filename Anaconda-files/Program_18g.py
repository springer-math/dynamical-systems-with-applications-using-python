# Program 18g: Edge detection on Lena image.
# See Figure 18.8.

import matplotlib.pyplot as plt
import skimage.io as io
from skimage.filters import roberts, sobel
from skimage.color import rgb2gray

lena = rgb2gray(io.imread('lena.jpg'))

edge_roberts = roberts(lena)
edge_sobel = sobel(lena)

fig, ax = plt.subplots(ncols=2, sharex=True, sharey=True, figsize=(8, 4))

ax[0].imshow(edge_roberts, cmap=plt.cm.gray)
ax[0].set_title('Roberts Edge Detection')

ax[1].imshow(edge_sobel, cmap=plt.cm.gray)
ax[1].set_title('Sobel Edge Detection')

for a in ax:
    a.axis('off')

plt.tight_layout()
plt.show()
