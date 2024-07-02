# #Find fft and verify it by ifft

# import numpy as np
# import matplotlib.pyplot as plt
# import scipy.fftpack as fftpack

# def sine(a,t):
#     return np.sin(np.pi*a*t*2)

# t = np.linspace(0,1,1000)
# y = 3*sine(1,t) + 1*sine(4,t) + 0.5*sine(7,t)

# # frequency vs phase spectrum

# Y = fftpack.fft(y)
# n = len(y)
# f = np.linspace(0,1,n)

# plt.plot(t,Y)
# plt.show()

# # Inverse Fast Fourier Transform
# y = fftpack.ifft(Y)
# plt.plot(t,y)
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

f1 = 1  # Frequency of first sinusoid
f2 = 4  # Frequency of second sinusoid
f3 = 7  # Frequency of third sinusoid
fs = 100  # Sampling frequency
t = np.linspace(0, 1, fs)  # Time vector

x = 3 * np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t) + 0.5 * np.sin(2 * np.pi * f3 * t)
X = np.fft.fft(x)
N = len(x)
xf = np.linspace(-fs/2, fs/2, N)
x_ifft = np.fft.ifft(X)

plt.plot(xf, np.abs(X))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid()
plt.title('FFT of the signal')
plt.show()

plt.plot(t, np.real(x_ifft), label='IFFT of X')
plt.plot(t, x, 'r--', label='Original Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.title('Original signal vs. IFFT of FFT')
plt.legend()
plt.show()

