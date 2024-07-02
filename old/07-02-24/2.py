import numpy as np
import matplotlib.pyplot as plt

# Define the function f(n) = a^n
def f(a, n):
    return a**n

# Define the Z-transform function
def z_transform(a, z):
    if np.abs(a) < np.abs(z):
        return 1 / (1 - a/z)
    else:
        return "Z-transform does not converge for |a| >= |z|"

# Generate a range of z values
z_values = np.linspace(0.1, 2, 1000)  # Avoiding zero to prevent division by zero

# Choose a value for a
a_value = 0.5

# Calculate the corresponding Z-transform values
z_transform_values = np.zeros_like(z_values, dtype=np.complex128)

for i, z in enumerate(z_values):
    if np.abs(a_value) < np.abs(z):
        z_transform_values[i] = 1 / (1 - a_value / z)
    else:
        z_transform_values[i] = np.nan

# Plot the magnitude and phase of the Z-transform
plt.figure(figsize=(12, 6))

# Plot the magnitude of the Z-transform
plt.subplot(2, 1, 1)
plt.plot(z_values, np.abs(z_transform_values))
plt.title(f'Magnitude of Z-transform: $|F(z)|$ for $f(n) = {a_value}^n$')
plt.xlabel('z')
plt.ylabel('Magnitude')
plt.grid(True)

# Plot the phase of the Z-transform
plt.subplot(2, 1, 2)
plt.plot(z_values, np.angle(z_transform_values))
plt.title(f'Phase of Z-transform: $\\angle F(z)$ for $f(n) = {a_value}^n$')
plt.xlabel('z')
plt.ylabel('Phase (radians)')
plt.grid(True)

plt.tight_layout()
plt.show()