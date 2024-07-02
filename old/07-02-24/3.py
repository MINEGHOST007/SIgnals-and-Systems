import numpy as np
import matplotlib.pyplot as plt


def z_transform(z):
    return z*(-3) / (1 - z*(-1))


z_values = np.linspace(0.1, 2, 1000) 
f_z_values = z_transform(z_values)


plt.plot(z_values, np.abs(f_z_values), label=r'$|F(z)|$')
plt.title('Magnitude of Z-transform')
plt.xlabel('Real Part of z')
plt.ylabel('Magnitude')
plt.legend()
plt.grid(True)
plt.show()