import numpy as np
import matplotlib.pyplot as plt

# Define the impulse response function h[n]
h_n = np.array([3, 2, 1, 1, 2])

# Define the input signal x
x = 2

# Define the output signal y[n] = h[n] * x
y_n = h_n * x

# Define the range of n
n = np.arange(0, len(h_n))

# Plot the impulse response
plt.stem(n, y_n, use_line_collection=True)
plt.xlabel('n')
plt.ylabel('y[n]')
plt.title('Output Signal')
plt.grid(True)
plt.show()
