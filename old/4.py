import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import ifft

# Define parameters
t = np.linspace(0.001, 10, 1000)  # Start time domain at a small positive value
f = ifft(1/t**2)

plt.figure()
plt.plot(t, f)
plt.grid()
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Inverse Laplace Transform of 1/s")
plt.show()