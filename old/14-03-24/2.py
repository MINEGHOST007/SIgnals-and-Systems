import numpy as np
import matplotlib.pyplot as plt

# Define the system function
def system_function(n):
    return np.sin(n)

# Discrete time values
n_values = np.arange(-10, 11)

# Input signal
x_n = np.sin(n_values)

# Output for original input
y_n_original = system_function(n_values)

# Delayed input
n_delayed = n_values - 2  # Adjust the delay as needed

# Output for delayed input
y_n_delayed = system_function(n_delayed)

# Plot original and delayed outputs
plt.stem(n_values, y_n_original, label='Original Input', basefmt='k-')
plt.stem(n_values, y_n_delayed, label='Delayed Input', basefmt='r--')
plt.xlabel('Discrete Time (n)')
plt.ylabel('Output (y(n))')
plt.title('System Time-Invariance Check')
plt.legend()
plt.show()