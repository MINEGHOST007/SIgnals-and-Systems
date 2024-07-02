import numpy as np
import matplotlib.pyplot as plt

# Define the Fourier series representation of a square wave
def square_wave(t, n_terms=10):
    x = np.zeros_like(t)
    for n in range(1, n_terms+1):
        x += np.sin((2*n - 1) * np.pi * t) / (2*n - 1)
    return (4 / np.pi) * x

# Sampling parameters
fs = 100  # Sampling frequency
T = 1 / fs  # Sampling period
t = np.arange(0, 1, T)  # Time vector

# Compute the signal
x = square_wave(t, n_terms=50)  # Use more terms for better approximation

# Compute the FFT
X = np.fft.fft(x)

# Compute the frequency axis
N = len(x)
frequencies = np.fft.fftfreq(N, d=T)

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