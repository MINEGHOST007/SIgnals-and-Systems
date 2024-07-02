import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft

t = np.linspace(0, 10, 1000)

F = fft(10/((t - 2)**2 + 20))

w = np.linspace(0, 1/t[1], len(t))

f = ifft(10/((t - 2)**2 + 20))

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(w, np.abs(F))
plt.grid()
plt.xlabel("Frequency (rad/s)")
plt.ylabel("Magnitude")
plt.title("Laplace Transform of F(s)")

plt.subplot(2, 1, 2)
plt.plot(t, f)
plt.grid()
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Inverse Laplace Transform of F(s)")

plt.subplots_adjust(hspace=0.5)
plt.show()