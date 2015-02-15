import numpy as np
import matplotlib.pyplot as plt
import csv

from mpl_toolkits.mplot3d import Axes3D

# Har delat upp datan i tre filer
Br = np.genfromtxt('Br')
print(Br[0,0:5]) # test att det ser ok ut

Bphi = np.genfromtxt('Bphi')
Bz = np.genfromtxt('Bz')


#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')

#plt.show()
#Axes3D.plot()
