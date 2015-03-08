import numpy as np
import matplotlib.pyplot as plt
import csv
from pylab import *
Br = np.transpose(np.genfromtxt('Output_B_r'))
Bz = np.transpose(np.genfromtxt('Output_B_z'))

R,Z = meshgrid(linspace(3.5,8.9,2*257), linspace(-5.5,5.5,2*513))
figure()
Q = quiver(R[::12,::12], Z[::12,::12], Br[::12,::12], Bz[::12,::12])
show()

