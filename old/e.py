import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft

a = 2  
t = np.linspace(0, 10, 1000)  

y = np.zeros_like(t)
y[t >= 2] = 1
y[t >= 3] += 1
y[t >= 2] -= 2 * t[t >= 2]

Y = fft(y)

f = np.linspace(0, 1/t[1], len(t))

y_inv = ifft(Y)

plt.figure()
plt.plot(f, np.abs(Y), label="Magnitude")
plt.grid()
plt.xlabel("Frequency (rad/s)")
plt.ylabel("Amplitude/Phase")
plt.title("Laplace Transform of y(t)")
plt.legend()

plt.figure()
plt.plot(t, y, label="Original Function", linestyle="--")
plt.plot(t, y_inv, label="Inverse Laplace Transform")
plt.grid()
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Inverse Laplace Transform Verification")
plt.legend()

plt.show()