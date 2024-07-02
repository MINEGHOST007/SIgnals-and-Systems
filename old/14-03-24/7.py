import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import convolve

# Define the impulse response h(t)
def impulse_response(t):
    return 8 * (t - 3) * (t >= 3)

# Define the input signal x(t)
def input_signal(t):
    return np.cos(t) + np.cos(7 * t)

# Time values
t_values = np.linspace(0, 10, 1000)

# Impulse response values
h_t = impulse_response(t_values)

# Input signal values
x_t = input_signal(t_values)

# Convolve input signal with impulse response to get output
y_t = convolve(x_t, h_t, mode='full') * (t_values[1] - t_values[0])  # Discrete convolution

# Trim the result to match the length of the input
y_t = y_t[:len(t_values)]

# Plot impulse response
plt.plot(t_values, h_t, label='Impulse Response (h(t))')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.title('Impulse Response of the LTI System')
plt.legend()
plt.show()

# Plot input signal
plt.plot(t_values, x_t, label='Input Signal (x(t))')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.title('Input Signal to the LTI System')
plt.legend()
plt.show()

# Plot output response
plt.plot(t_values, y_t, label='Output Response (y(t))')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.title('Output Response of the LTI System')
plt.legend()
plt.show()