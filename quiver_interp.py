import numpy as np
import matplotlib.pyplot as plt
import csv
from pylab import *
Br_short = np.transpose(np.genfromtxt('Output_B_r_short'))
Bz_short = np.transpose(np.genfromtxt('Output_B_z_short'))

Br = np.transpose(np.genfromtxt('Br'))
Bz = np.transpose(np.genfromtxt('Bz'))

R,Z = meshgrid(linspace(3.5,8.9,257), linspace(-5.5,5.5,513))
figure()
Q = quiver(R[::12,::12], Z[::12,::12], Br[::12,::12], Bz[::12,::12])
#show()

# för testing purposes
#print("real: ",Br[153,88])
#print("interp: ", Br_short[153,88])
