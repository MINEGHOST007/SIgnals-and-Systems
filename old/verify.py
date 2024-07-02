import numpy as np
import matplotlib.pyplot as plt

def plotall(x,h):
    plt.subplot(3,1,1)
    plt.stem(range(len(x)),x,label='x(n)*h(n)')

    plt.subplot(3,1,2)
    plt.stem(range(len(h)),h,label='h(n)*x(n)')

    plt.tight_layout()
    plt.show()

x = np.array([1,2,3])

h = np.array([0.5,1,0.5])

lhs = np.convolve(x,h,mode="full")
rhs = np.convolve(h,x,mode="full")

if np.array_equal(lhs,rhs):
    print("Verified")
else:
    print("Not Verified")

plotall(lhs,rhs)
