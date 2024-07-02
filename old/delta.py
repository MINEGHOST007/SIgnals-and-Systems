import numpy as np
import matplotlib.pyplot as plt

def dirac(n):
    return np.where(n==0,1,0)

def unit(n):
    return np.where(n>=0,1,0)

def x(n):
    return 3*dirac(n+2)-dirac(n-1)+2*dirac(n-3)

def h(n):
    return unit(n+4)-unit(n-3)
def convolute(x,h,n):
    y = np.convolve(x,h,mode="full")
    n_y = np.arange(2*min(n),2*max(n)+1)
    return n_y,y

def plotit(ax,n,signal):
    ax.stem(n,signal)
    
n = np.arange(-25,26)
x = x(n)
h = h(n)
n_y,y = convolute(x,h,n)

fig,axes= plt.subplots(3,1,figsize = (10,8),sharex=True)

plotit(axes[0],n,x)
plotit(axes[1],n,h)
plotit(axes[2],n_y,y)

plt.xlabel('n')
plt.tight_layout()
plt.show()