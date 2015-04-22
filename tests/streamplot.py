import numpy as np
import matplotlib.pyplot as plt
import csv

from pylab import *

# wall
contour = np.genfromtxt('iter.wall_2d', delimiter='', skip_header=5)

r_contour = contour[:,0]
z_contour = contour[:,1]

plt.plot(r_contour,z_contour, color='k', linewidth=4)

#field
Br = np.transpose(np.genfromtxt('Br'))
Bz = np.transpose(np.genfromtxt('Bz'))

R,Z = meshgrid(linspace(3.5,8.9,257), linspace(-5.5,5.5,513))

plt.streamplot(R, Z, Br, Bz, color='k', linewidth=1)

plt.axis('equal')

plt.xlabel(r'$r$ (m)', fontsize=17)
plt.ylabel(r'$z$ (m)', fontsize=17)

show()
