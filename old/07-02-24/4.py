import numpy as np
import matplotlib.pyplot as plt

def f(n):
    return (1/4)**n * (n >= 0)

def z_transform(z):
    if np.abs(z) > 4:
        return 1 / (1 - (1/4) / z)
    else:
        return "Z-transform does not converge for |z| <= 4"

z_values = np.linspace(4.1, 5, 1000) 
z_transform_values = np.array([z_transform(z) for z in z_values])

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(z_values, np.abs(z_transform_values))
plt.title('Magnitude of Z-transform: $|F(z)|$ for $f(n) = \\left(\\frac{1}{4}\\right)^n u(n)$')
plt.xlabel('z')
plt.ylabel('Magnitude')
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(z_values, np.angle(z_transform_values))
plt.title('Phase of Z-transform: $\\angle F(z)$ for $f(n) = \\left(\\frac{1}{4}\\right)^n u(n)$')
plt.xlabel('z')
plt.ylabel('Phase (radians)')
plt.grid(True)

plt.tight_layout()
plt.show()