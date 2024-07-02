import matplotlib.pyplot as plt
import numpy as np
import math

fig = plt.figure()
axes = fig.add_axes([0.1,0.1,0.8,0.8])

minx = int(input("Enter minimum x : "))
miny = int(input("Enter minimum y : "))

maxx = int(input("Enter maximum x : "))
maxy = int(input("Enter maximum y : "))

axes.set_xlim([minx,maxx])
axes.set_ylim([miny,maxy])

n = int(input("Enter graph x maxlimit as x PI : "))
s = int(input("Enter graph x minlimit as x PI : ('you can enter negative') "))
x = np.arange(s*np.pi,n*np.pi,0.1)
y = np.sin(x)

axes.plot(x,y)
plt.show()