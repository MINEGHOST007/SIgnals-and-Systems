import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

# Define parameters
t = np.linspace(0, 10, 1000)  # Define the time domain

# Define the functions
f = np.zeros_like(t)
f[t <= 3] = 1

g = np.ones_like(t)
g[t >= 3] = 0

# Calculate the Laplace transforms
F = fft(f)
G = fft(g)

# Create the frequency domain
w = np.linspace(0, 1/t[1], len(t))

# Plot the magnitudes of the Laplace transforms
plt.figure()
plt.plot(w, np.abs(F), label="F(s)")

plt.grid()
plt.xlabel("Frequency (rad/s)")
plt.ylabel("Magnitude")
plt.title("Laplace Transforms of f(t)")
plt.legend()
plt.show()

plt.figure()
plt.plot(w, np.abs(G), label="G(s)")
plt.grid()
plt.xlabel("Frequency (rad/s)")
plt.ylabel("Magnitude")
plt.title("Laplace Transforms of g(t)")
plt.legend()
plt.show()