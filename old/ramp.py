import matplotlib.pyplot as plt
import numpy as np

def findy(i):
    if i<0 :
        return 0
    else:
        return i

fig = plt.figure()

axes = fig.add_axes([0.1,0.1,0.8,0.8])

minx = int(input("Enter minimum x : "))
miny = int(input("Enter minimum y : "))

maxx = int(input("Enter maximum x : "))
maxy = int(input("Enter maximum y : "))

axes.set_xlim([minx,maxx])
axes.set_ylim([miny,maxy])

for i in range(minx,maxx):
    ypoints = np.array([0, findy(i)])
    xpoints = np.array([i,i])
    axes.plot(xpoints,ypoints,marker='o')
plt.show()

