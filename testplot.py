import numpy as np
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.plot([1,2],[3,3],[0,0]) # testvektorer i x,y och z riktning

plt.show()
Axes3D.plot()
