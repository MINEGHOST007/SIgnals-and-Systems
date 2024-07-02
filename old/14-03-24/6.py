import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, step
from scipy.integrate import odeint

# Define the system response and input function
def system_output(t):
    return 2 * np.exp(t)

def input_function(t):
    return np.heaviside(t, 1)

# Time values
t_values = np.linspace(0, 5, 1000)

# Calculate the system output using the given response
y_values = system_output(t_values)

# Plot the system output
plt.plot(t_values, y_values, label='System Output (2e^t u(t))')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.title('System Output')
plt.legend()
plt.show()

# Simulate and calculate the system function from the input and output
t_sim = np.linspace(0, 5, 1000)
output_sim = odeint(lambda y, t: 2 * np.exp(t), 0, t_sim)[:, 0]
t, y = step(TransferFunction([2], [1, -1, -2]), T=t_sim)
 
# Plot the simulated system response
plt.plot(t, y, label='Simulated System Response')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.title('Simulated System Response')
plt.legend()
plt.show()