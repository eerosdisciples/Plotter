import matplotlib.pyplot as plt
import numpy as np
import csv
import matplotlib.cbook as cbook

fig = plt.figure()

results = np.genfromtxt('../ode-solver/particle.csv', delimiter=',', skip_header=8)

T = results[:,0]
E = results[:,3]

plt.plot(T,E, color='r')

plt.xlabel('Time (s)')
plt.ylabel('Energy (eV)')

plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))



plt.grid()
plt.show()

