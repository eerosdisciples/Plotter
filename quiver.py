import numpy as np
import matplotlib.pyplot as plt
import csv

from pylab import *

Br = np.genfromtxt('Br')
Bz = -np.genfromtxt('Bz')

R,Z = meshgrid(linspace(3.5,8.9,257), linspace(-5.5,5.5,513))

figure()
Q = quiver(R[::12,::12], Z[::12,::12], Br[::12,::12], Bz[::12,::12])
#quiver(Br[::12,::12],Bz[::12,::12])
#qk = quiverkey(Q, 0.5, 0.92, 2, r'$2 \frac{m}{s}$', labelpos='W',
#        fontproperties={'weight':'bold'})

show()

#l,r,b,t = axis()
#dx,dy = r-l,t-b
