import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

np.random.seed(42)
n_samples = 100
n_values = np.arange(n_samples)
x = np.sin(0.2 * n_values) + 0.5 * np.random.normal(size=n_samples)

h1 = np.ones(3) / 3
h2 = np.ones(7) / 7
h3 = np.ones(11) / 11

y1 = convolve(x, h1, mode='full')[:n_samples]
y2 = convolve(x, h2, mode='full')[:n_samples]
y3 = convolve(x, h3, mode='full')[:n_samples]

plt.figure(figsize=(12, 10))

plt.subplot(411)
plt.plot(n_values, x, label='x(n)')
plt.title('Input Signal x(n)')
plt.xlabel('n')
plt.legend()

plt.subplot(412)
plt.plot(n_values, y1, label='y(n) with h1')
plt.title('Convolution Result with h1')
plt.xlabel('n')
plt.legend()

plt.subplot(413)
plt.plot(n_values, y2, label='y(n) with h2')
plt.title('Convolution Result with h2')
plt.xlabel('n')
plt.legend()

plt.subplot(414)
plt.plot(n_values, y3, label='y(n) with h3')
plt.title('Convolution Result with h3')
plt.xlabel('n')
plt.legend()

plt.tight_layout()
plt.show()