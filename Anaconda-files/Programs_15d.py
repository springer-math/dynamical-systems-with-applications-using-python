# Programs 15d: Plotting a Newton fractal.
# See Figure 15.7.

from PIL import Image
imgx = 512;imgy = 512
image = Image.new("RGB",(imgx,imgy))

xmin=-1.5;xmax=1.5;ymin=-1.5;ymax=1.5;

Max_iter = 20     
h=1e-6            # Step size.
eps=1e-3          # Maximum error.

def f(z):
    return z**3 - 1.0  # Complex function.

# Draw the fractal.
for y in range(imgy):
    zy = y * (ymax - ymin) / (imgy - 1) + ymin
    for x in range(imgx):
        zx = x * (xmax - xmin) / (imgx - 1) + xmin
        z = complex(zx, zy)
        for i in range(Max_iter):
            # Complex numerical derivative.
            dz = (f(z + complex(h, h)) - f(z)) / complex(h, h)
            z0 = z - f(z) / dz    # Newton iteration.
            if abs(z0 - z) < eps: # Stop when close enough to any root.
                break
            z = z0
        image.putpixel((x, y), (i % 4 * 64, i % 8 * 32, i % 16 * 16))

image.save("Newton_Fractal.png", "PNG")