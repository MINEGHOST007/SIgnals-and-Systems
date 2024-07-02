import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([3,3])
ypoints = np.array([0, 1])

fig = plt.figure()

axes = fig.add_axes([0.1,0.1,0.8,0.8])

axes.set_xlim([0,5])
axes.set_ylim([0,3])

axes.plot(xpoints, ypoints,marker='o')
plt.show()
