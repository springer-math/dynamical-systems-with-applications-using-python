# Programs 15c: The Mandelbrot set.
# See Figure 15.3.

import numpy as np
import matplotlib.pyplot as plt
xmin=-2.5;xmax=1;ymin=-1.5;ymax=1.5;
xrange=xmax-xmin;yrange=ymax-ymin;

def mandelbrot(h,w, Max_it=50):
     y,x = np.ogrid[ ymin:ymax:h*1j, xmin:xmax:w*1j ]
     c = x+y*1j
     z = c
     Div_iter = Max_it + np.zeros(z.shape, dtype=int)

     for i in range(Max_it):
         z = z**2 + c
         Div_test = z*np.conj(z) > 2**2            
         Div_num = Div_test & (Div_iter==Max_it)  
         Div_iter[Div_num] = i                 
         z[Div_test] = 2                        

     return Div_iter                 # Number of iterations to diverge.

scale=1000                           # Amount of detail in the set.

# Set the tick labels to the Argand plane.
fig, ax = plt.subplots()
ax.imshow(mandelbrot(scale,scale))
xtick_labels = np.linspace(xmin, xmax, xrange / 0.5)
ax.set_xticks([(x-xmin) / xrange * scale for x in xtick_labels])
ax.set_xticklabels(['{:.1f}'.format(xtick) for xtick in xtick_labels])
ytick_labels = np.linspace(ymin, ymax, yrange / 0.5)
ax.set_yticks([-(y+ymin) / yrange * scale for y in ytick_labels])
ax.set_yticklabels(['{:.1f}'.format(ytick) for ytick in ytick_labels])
plt.show()