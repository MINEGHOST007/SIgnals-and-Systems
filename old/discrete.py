import numpy as np
import matplotlib.pyplot as plt

def convolute(x,h):
    y = np.convolve(x,h,mode="full")
    return y

def plotall(x,h,y):
    plt.subplot(3,1,1)
    plt.stem(range(len(x)),x,label='x(n)')

    plt.subplot(3,1,2)
    plt.stem(range(len(h)),h,label='h(n)')
    
    plt.subplot(3,1,3)
    plt.stem(range(len(y)),y,label='y(n)')

    plt.tight_layout()
    plt.show()

def analytic(x,h):
    y = np.convolve(x,h)
    return  y

x = np.array([1,2,3])
h = np.array([0.5,1,0.5])
y = convolute(x,h)

y_analytic = analytic(x,h)

if np.array_equal(y,y_analytic):
    print("Verified")
else:
    print("Not Verified")

plotall(x,h,y)