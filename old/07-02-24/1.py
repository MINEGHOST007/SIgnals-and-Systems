import numpy as np
import matplotlib.pyplot as plt

# Define the function f(k) = sin(k)
def f(k):
    return np.sin(k)

# Define the Z-transform function
def z_transform_sine(z):
    return np.sin(np.angle(z)) / (1 - 2 * np.cos(np.angle(z)) * z*(-1) + z*(-2))

# Generate a range of z values
z_values = np.linspace(0.1, 2, 1000)  # Avoiding zero to prevent division by zero

# Calculate the corresponding Z-transform values
z_transform_values = np.zeros_like(z_values, dtype=np.complex128)

for i, z in enumerate(z_values):
    z_transform_values[i] = z_transform_sine(z)

# Plot the magnitude and phase of the Z-transform
plt.figure(figsize=(12, 6))

# Plot the magnitude of the Z-transform
plt.subplot(2, 1, 1)
plt.plot(z_values, np.abs(z_transform_values))
plt.title('Magnitude of Z-transform: $|F(z)|$ for $f(k) = \\sin(k)$')
plt.xlabel('Re(z)')
plt.ylabel('Magnitude')
plt.grid(True)

# Plot the phase of the Z-transform
plt.subplot(2, 1, 2)
plt.plot(z_values, np.angle(z_transform_values))
plt.title('Phase of Z-transform: $\\angle F(z)$ for $f(k) = \\sin(k)$')
plt.xlabel('Re(z)')
plt.ylabel('Phase (radians)')
plt.grid(True)

plt.tight_layout()
plt.show()