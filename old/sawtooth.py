import numpy as np
import matplotlib.pyplot as plt

def generate_asymmetric_sawtooth_waveform(period, duration, amplitude, slope, num_periods):
    t = np.linspace(0, period * num_periods, 1000 * num_periods)
    sawtooth = amplitude * (t % period) / period + slope * (t // period)
    return t, sawtooth


period = 1.0  
duration = 0.8 
amplitude = 1.0  
slope = 0 

num_periods = 5 


time, waveform = generate_asymmetric_sawtooth_waveform(period, duration, amplitude, slope, num_periods)


plt.plot(time, waveform)
plt.title('Asymmetric Sawtooth Waveform')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()