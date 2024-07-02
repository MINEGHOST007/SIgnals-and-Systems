import numpy as np
import matplotlib.pyplot as plt

# Define the signal
def signal(t, A, f, phi):
    return A * np.cos(2 * np.pi * f * t + phi)

# Sampling parameters
fs = 100  # Sampling frequency
T = 1 / fs  # Sampling period
t = np.arange(0, 1, T)  # Time vector

# Signal parameters
A = 5  # Amplitude
f = 10  # Frequency in Hz
phi = np.pi / 4  # Phase angle in radians

# Compute the signal
x = signal(t, A, f, phi)

# Compute the FFT
X = np.fft.fft(x)

# Compute the frequency axis
N = len(x)
frequencies = np.fft.fftfreq(N, d=(T))

# Plot the frequency spectrum
plt.figure(figsize=(10, 6))
plt.plot(frequencies, np.abs(X))
plt.title('Frequency Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid()
plt.show()

# Verify by computing the IFFT
x_restored = np.fft.ifft(X)

# Plot the original signal and the restored signal
plt.figure(figsize=(10, 6))
plt.plot(t, x, label='Original Signal')
plt.plot(t, x_restored, label='Restored Signal', linestyle='--')
plt.title('Original Signal vs. Restored Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()
plt.show()