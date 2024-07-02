import matplotlib.pyplot as plt
import numpy as np

def periodic_function(x):
    period = 4
    return np.sign(np.sin(2 * np.pi / period * x))

fig = plt.figure()
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
import numpy as np
import matplotlib.pyplot as plt

def generate_rectangular_pulse(period, duration, amplitude, num_periods):
    t = np.linspace(0, period * num_periods, 1000 * num_periods)
    
    pulse = amplitude * (np.floor(t / period) % 2 == 0)
    
    return t, pulse

period = 1.0 
duration = 0.2  
amplitude = 1.0  
num_periods = 5 

time, pulse = generate_rectangular_pulse(period, duration, amplitude, num_periods)


plt.plot(time, pulse)
plt.title('Periodic Rectangular Pulse')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()
minx = int(input("Enter minimum x: "))
miny = int(input("Enter minimum y: "))

maxx = int(input("Enter maximum x: "))
maxy = int(input("Enter maximum y: "))

axes.set_xlim([minx, maxx])
axes.set_ylim([miny, maxy])

x_values = np.linspace(minx, maxx, 1000)

y_values = periodic_function(x_values)

axes.plot(x_values, y_values, label='Periodic Function')

axes.set_xlabel('X-axis')
axes.set_ylabel('Y-axis')
axes.set_title('Rectangular Periodic Graph')

axes.legend()

plt.show()
