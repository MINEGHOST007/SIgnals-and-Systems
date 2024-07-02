import numpy as np
import matplotlib.pyplot as plt

# Define the system function
def system_function(t):
    return np.exp(t)

# Time values
t_values = np.linspace(-5, 5, 100)

# Input signal
x_t = np.exp(t_values)

# Output for original input
y_t_original = system_function(t_values)

# Delayed input
t_delayed = t_values - 2  # Adjust the delay as needed

# Output for delayed input
y_t_delayed = system_function(t_delayed)

# Plot original and delayed outputs
plt.plot(t_values, y_t_original, label='Original Input')
plt.plot(t_values, y_t_delayed, label='Delayed Input')
plt.xlabel('Time (t)')
plt.ylabel('Output (y(t))')
plt.title('System Time-Invariance Check')
plt.legend()
plt.show()