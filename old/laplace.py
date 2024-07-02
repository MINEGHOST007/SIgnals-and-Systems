import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft

t = np.linspace(0, 10, 1000)
a = 2  

y = t**2

# y = np.exp(-a * t) + np.exp(-3 * a * t)

# y = np.exp(2 * t) * np.sin(2*t)

# y = np.exp(3*t)+ np.cos(6*t)-np.exp(-3 * t) * np.cos(6*t)

Y = fft(y)

f = np.linspace(0, 1/t[1], len(t))

plt.figure()
plt.plot(f, np.abs(Y), label="Magnitude")
plt.grid()
plt.xlabel("Frequency (rad/s)")
plt.ylabel("Amplitude/Phase")
plt.title("Laplace Transform of y(t)")
plt.legend()
plt.show()

y_inv = ifft(Y)

plt.figure()
plt.plot(t, y, label="Original Function", linestyle="--")
plt.plot(t, y_inv, label="Inverse Laplace Transform")
plt.grid()
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Inverse Laplace Transform Verification")
plt.legend()
plt.show()