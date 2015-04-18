import numpy as np
import matplotlib.pyplot as plt
import csv
import argparse

from pylab import *


parser = argparse.ArgumentParser()
parser.add_argument('filenumber')
args = parser.parse_args()


# wall
contour = np.genfromtxt('iter.wall_2d', delimiter='', skip_header=5)

r_contour = contour[:,0]
z_contour = contour[:,1]

plt.plot(r_contour,z_contour, color='r', linewidth=2)

#field
Br = np.transpose(np.genfromtxt('Br'))
Bz = np.transpose(np.genfromtxt('Bz'))

R,Z = meshgrid(linspace(3.5,8.9,257), linspace(-5.5,5.5,513))

plt.streamplot(R, Z, Br, Bz, linewidth=0.5)

# trajectory

root = '../../massive-octo-tribble/sims5/particle'

filenr = args.filenumber

suffix ='.csv'

file = root+filenr+suffix

results = np.genfromtxt(file, delimiter=',', skip_header=8)

x = results[:,2]
y = results[:,3]
z = results[:,4]

r = np.sqrt(x**2 + y**2)

plt.plot(r,z, linewidth=3, color='k')

# plot
plt.axis('equal')

plt.xlabel(r'$r$ (m)', fontsize=17)
plt.ylabel(r'$z$ (m)', fontsize=17)

show()
