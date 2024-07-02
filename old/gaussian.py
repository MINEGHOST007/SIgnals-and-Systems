import numpy as np
import matplotlib.pyplot as plt

amplitude = 1.0
frequency = 1.0
sigma = 0.1
duration = 2.0
num_samples = 2000

t = np.linspace(0, duration, num_samples)

pulse = amplitude * np.exp(-((t % (1/frequency)) - 0.5*(1/frequency))**2 / (2*sigma**2))

plt.plot(t, pulse)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Periodic Gaussian Pulse')
plt.grid(True)
plt.show()