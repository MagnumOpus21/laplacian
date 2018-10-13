import math
from scipy.interpolate import spline
import matplotlib.pyplot as plt
import numpy as np

def gaussian(i, sigma):
    return math.exp(-i**2 / (2*sigma**2)) / sigma

def laplacian(i, sigma):
    return gaussian(i,sigma)/sigma**2 * (((i**2)/(sigma**2))-1)


g, g2 = [], []
l = []

x = [i for i in range(-10,10)]

for i in range(-10,10):
    g.append(gaussian(i, 2.6))
    g2.append(gaussian(i,1.6))
    l.append(laplacian(i,1.65))

g = list(map(lambda x : x[0]-x[1], zip(g,g2)))

g_np = np.array(g)
l_np = np.array(l)

x_points = np.linspace(-10,10,500)

g_smooth = spline(x, g, x_points)
l_smooth = spline(x, l_np, x_points)

plt.plot(g_smooth, label = "DoG")
plt.plot(l_smooth, label = 'LoG')
plt.gca().legend(("DoG", "LoG"))
plt.show()