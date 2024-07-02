import numpy as np
import matplotlib.pyplot as plt


def f(n):
    return 2*(n+1) + 4 * (1/2)*n


def z_transform(z):
    term1 = 2 * z / (z - 2)
    term2 = 4 * z / (z - 0.5)
    return term1 + term2


z_values = np.linspace(0.6, 2, 1000)  

z_transform_values = z_transform(z_values)


plt.figure(figsize=(12, 6))


plt.subplot(2, 1, 1)
plt.plot(z_values, np.abs(z_transform_values))
plt.title('Magnitude of Z-transform: $|F(z)|$ for $f(n) = 2^{(n+1)} + 4 \\left(\\frac{1}{2}\\right)^n$')
plt.xlabel('z')
plt.ylabel('Magnitude')
plt.grid(True)


plt.subplot(2, 1, 2)
plt.plot(z_values, np.angle(z_transform_values))
plt.title('Phase of Z-transform: $\\angle F(z)$ for $f(n) = 2^{(n+1)} + 4 \\left(\\frac{1}{2}\\right)^n$')
plt.xlabel('z')
plt.ylabel('Phase (radians)')
plt.grid(True)

plt.tight_layout()
plt.show()