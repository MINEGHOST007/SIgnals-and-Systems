import numpy as np
import matplotlib.pyplot as plt

# Define the range of n
n = np.arange(0, 10)

# Define the impulse response function h[n]
h_n = (0.5)**n

# Plot the impulse response
plt.stem(n, h_n, use_line_collection=True)
plt.xlabel('n')
plt.ylabel('h[n]')
plt.title('Impulse Response of the System')
plt.grid(True)
plt.show()
