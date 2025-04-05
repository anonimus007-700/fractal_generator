import numpy as np
import matplotlib.pyplot as plt

x_start, y_start = -2, -2
width, height = 4, 4
density_per_unit = 1680  # increased density to add more pixels per unit

# real and imaginary axis
re = np.linspace(x_start, x_start + width, width * density_per_unit )
im = np.linspace(y_start, y_start + height, int(height * density_per_unit * (1080/1680)))  # scale the height to 1080 pixels


threshold = 100

# we represent c as c = r*cos(a) + i*r*sin(a) = r*e^{i*a}
r = 0.7885
a = 21

fig = plt.figure(figsize=(16.8, 10.8))
ax = plt.axes()

def julia_quadratic(zx, zy, cx, cy, threshold):
    z = complex(zx, zy)
    c = complex(cx, cy)

    for i in range(threshold):
        z = z**2 + c
        if abs(z) > 4.:
            return i

    return threshold - 1

X = np.empty((len(im), len(re)))
cx, cy = r * np.cos(a), r * np.sin(a)

for i in range(len(im)):
    for j in range(len(re)):
        X[i, j] = julia_quadratic(re[j], im[i], cx, cy, threshold)

img = plt.imshow(X, interpolation="bicubic", cmap='hot')
plt.axis('off')  # turn off the axis
plt.savefig('julia.png', bbox_inches='tight', pad_inches=0, dpi=300)

