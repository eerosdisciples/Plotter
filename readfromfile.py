import numpy as np
import matplotlib.pyplot as plt
import csv

from mpl_toolkits.mplot3d import Axes3D

# Har delat upp datan i tre filer
Br = np.genfromtxt('Br')
#print(Br) # test att det ser ok ut

Bphi = np.genfromtxt('Bphi')
Bz = np.genfromtxt('Bz')

plt.xlabel('r')
plt.ylabel('z')

imgplot = plt.imshow(Br, origin='lower')
plt.show()

  

#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')

#plt.show()
#Axes3D.plot()
