# # Fast Fourier Transform
# import numpy as np
# import matplotlib.pyplot as plt
# import scipy.fftpack as fftpack

# def sine(a,t):
#     return np.sin(np.pi*a*t)

# t = np.linspace(0,1,1000)
# y = 10*sine(400,t) + 5*sine(600,t) + 12*sine(800,t)

# # frequency vs phase spectrum

# Y = fftpack.fft(y)
# n = len(y)
# f = np.linspace(0,1,n)
# plt.plot(f,np.abs(Y))
# plt.show()


import numpy as np
import matplotlib.pyplot as plt

def fft(x):
    N = len(x)
    if N <= 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    even = np.pad(even, (0, N - len(even)), 'constant')  # Zero-padding
    odd = np.pad(odd, (0, N - len(odd)), 'constant')     # Zero-padding
    T = [np.exp(-2j * np.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]

# Define the signal
def signal(t):
    return 10*np.sin(400*np.pi*t) + 5*np.sin(800*np.pi*t) + 12*np.sin(600*np.pi*t)

fs = 100  # Sampling frequency
T = 1/fs   # Sampling period
t = np.arange(0, 1, T)  # Time vector

# Compute the signal
y = signal(t)

# Compute the FFT
Y = fft(y)

# Compute the frequency axis
N = len(y)
frequencies = np.linspace(0.0, 1.0/(2.0*T), N//2)

# Plot the frequency spectrum
plt.plot(frequencies, 2.0/N * np.abs(Y[:N//2]))
plt.title('Frequency Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()