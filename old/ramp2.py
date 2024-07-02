import matplotlib.pyplot as plt
import numpy as np



fig = plt.figure()

axes = fig.add_axes([0.1,0.1,0.8,0.8])

minx = int(input("Enter minimum x : "))
miny = int(input("Enter minimum y : "))

maxx = int(input("Enter maximum x : "))
maxy = int(input("Enter maximum y : "))

axes.set_xlim([minx,maxx])
axes.set_ylim([miny,maxy])

for i in range(minx,maxx):
    if i< 0:
        axes.plot(i,0,marker='o')
    else:
        axes.plot(i,i,marker='o')
plt.show()

