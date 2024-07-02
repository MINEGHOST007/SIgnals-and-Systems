import numpy as np
import matplotlib.pyplot as plt

def valuex(t):
    if t < 0 or t >=12:
        return 0
    elif t>=8 and t<12:
        return 5
    elif t>=5 and t<8:
        return 2
    elif t>=0 and t<5:
        return 1
    else:
        return 0

def valuey(t):
    if t < 0 or t >=15:
        return 0
    elif t>=10 and t<15:
        return 7
    elif t>=7 and t<10:
        return 0
    elif t>=0 and t<7:
        return 2
    else:
        return 0

t = np.arange(-5,20,1)
u = []
c = int(input("Enter your choice : 1 - 2\n"))
for i in range(len(t)):
    if c == 1:
        temp = valuex(-3*t[i]+2)+valuey(3*t[i]-2)
    elif c ==2:
        temp =  valuex(0.5*t[i]-2)*valuey(t[i])
    u.append(temp)
plt.plot(t,u)
plt.show()