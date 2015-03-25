import matplotlib.pyplot as plt
import numpy as np
import csv
from mpl_toolkits.mplot3d import Axes3D

results = np.genfromtxt('../ode-solver/particle.csv', delimiter=',', skip_header=8)

x = results[:,2]
y = results[:,3]
z = results[:,4]

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(x,y,z)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.invert_xaxis()
ax.invert_yaxis()

plt.show()
