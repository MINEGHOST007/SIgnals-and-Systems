import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import impulse, lti, step

# Define the system's differential equation coefficients
numerator = [1]
denominator = [1, -1, -2]

# Create a transfer function based on the coefficients
system = lti(numerator, denominator)

# Time values
t_values = np.linspace(0, 10, 1000)

# Impulse response
t_impulse, y_impulse = impulse(system, T=t_values)

# Step response (for visualization)
t_step, y_step = step(system, T=t_values)

# Plot impulse response
plt.plot(t_impulse, y_impulse, label='Impulse Response')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.title('Impulse Response of the System')
plt.legend()
plt.show()

# Plot step response (for visualization)
plt.plot(t_step, y_step, label='Step Response')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.title('Step Response of the System')
plt.legend()
plt.show()