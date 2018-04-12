# Program 18f: Fourier transform of a Lena image.
# See Figure 18.7.

import numpy as np
import skimage.io as io
import pylab
import matplotlib.pyplot as plt
from skimage.color import rgb2gray

lena = rgb2gray(io.imread('lena.jpg'))

fig1 = plt.figure()
plt.imshow(lena, cmap='gray')

fig2 = plt.figure()
# Take the 2-dimensional DFT and centre the frequencies
ftimage = np.fft.fft2(lena)
ftimage = np.fft.fftshift(ftimage)
ftimage = np.abs(ftimage)
fftimage = np.log(ftimage)
fftimage = rgb2gray(fftimage)
pylab.imshow(fftimage, cmap='gray')
plt.show()

""" ???
# Apply a crude filter.
fftimage[300:400, 300:400] = 0
fig3 = plt.figure()
pylab.imshow(fftimage, cmap='gray')

fig4 = plt.figure()
# Finally, take the inverse transform and show the blurred image
imagep = np.fft.ifft2(fftimage)
imagep = image.formarray(imagep)
imagep.show()
#pylab.imshow(np.abs(imagep), cmap='gray')
"""
