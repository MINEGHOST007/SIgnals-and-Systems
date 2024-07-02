import numpy as np
import matplotlib.pyplot as plt

# Define the system function
def system_output(t, x):
    return t * x

# Define the input signal
def input_signal(t):
    return np.sin(t)  # You can change the input signal here

# Define the time shift
delta_t = 1

# Time range
t_range = np.linspace(-5, 5, 1000)

# Input and output signals without time shift
x = input_signal(t_range)
y = system_output(t_range, x)

# Input signal with time shift
x_shifted = input_signal(t_range - delta_t)
y_shifted = system_output(t_range, x_shifted)

# Plotting
plt.figure(figsize=(10, 5))

plt.subplot(2, 1, 1)
plt.plot(t_range, x, label='Input Signal $x(t)$')
plt.plot(t_range, y, label='Output Signal $y(t)$')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Original Signals')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t_range, x_shifted, label='Shifted Input Signal $x(t - \Delta t)$')
plt.plot(t_range, y_shifted, label='Output Signal $y(t)$ with Shifted Input')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Shifted Signals')
plt.legend()

plt.tight_layout()
plt.show()