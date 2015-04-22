import matplotlib.pyplot as plt
import numpy as np
import csv
import matplotlib.cbook as cbook

# wall
contour = np.genfromtxt('iter.wall_2d', delimiter='', skip_header=5)

r_contour = contour[:,0]
z_contour = contour[:,1]

plt.plot(r_contour,z_contour, color='r')


# trajectory
fig = plt.figure()

results = np.genfromtxt('../../ode-solver/particle.csv', delimiter=',', skip_header=8)

x = results[:,2]
y = results[:,3]
z = results[:,4]

r = np.sqrt(x**2 + y**2)

plt.plot(r,z)

#field
Br = np.transpose(np.genfromtxt('Br'))
Bz = np.transpose(np.genfromtxt('Bz'))

R,Z = meshgrid(linspace(3.5,8.9,257), linspace(-5.5,5.5,513))

plt.streamplot(R, Z, Br, Bz, linewidth=1)

# plot
plt.axis('equal')

plt.xlabel(r'$r$ (m)')
plt.ylabel(r'$z$ (m)')

plt.grid()
plt.show()
#

