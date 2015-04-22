import numpy as np
import matplotlib.pyplot as plt
import csv

from pylab import *

Br = np.transpose(np.genfromtxt('Br'))
Bz = np.transpose(np.genfromtxt('Bz'))

R,Z = meshgrid(linspace(3.5,8.9,257), linspace(-5.5,5.5,513))

plt.streamplot(R, Z, Br, Bz, color= Br, linewidth=1, cmap=plt.cm.autumn )
plt.colorbar()

show()
