# Programs_18d: Color picture of a raccoon.
# See Figure 18.2.

from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
face = misc.face()

fig1 = plt.figure()
plt.imshow(face)

print('Dimensions=',face.shape)     # Dimensions ofimage.
print('RGB value=',face[100,100])  # RGB values of pixel.
WhitePixels=np.zeros((767,1023))    # The number of white pixels.

for i in range(767):
    for j in range(1023):
        if face[i,j][0]>180 and face[i,j][1]>180 and face[i,j][2]>180:
            WhitePixels[i,j]=1

fig2 = plt.figure()
plt.imshow(WhitePixels,cmap='gray')
print('There are',int(np.sum(WhitePixels)),'white pixels.')
plt.show()
