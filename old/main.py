import matplotlib.pyplot as plt
import numpy as np
import random

def findy(xpoint,user):
    print(xpoint)   
    if xpoint%user==0:
        return random.randint(0,8)
    else:
        return 0

fig = plt.figure()

axes = fig.add_axes([0.1,0.1,0.8,0.8])

min = int(input("Enter minimum x : "))

max = int(input("Enter maximum x : "))

axes.set_xlim([min,max])
axes.set_ylim([0,10])

user = int(input("Enter a number between "+ str(min) + " and " + str(max) + " :"))

for i in range(min,max):
    ypoints = np.array([0, findy(i,user)])
    xpoints = np.array([i,i])
    axes.plot(xpoints,ypoints,marker='o')
plt.show()