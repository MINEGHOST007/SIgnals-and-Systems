from sympy import symbols, Heaviside, laplace_transform, lambdify
import matplotlib.pyplot as plt
import numpy as np

t, s = symbols('t s')

f_t = Heaviside(t**2) * Heaviside(4 - t)
g_t = Heaviside(t) - Heaviside(t - 4)

F_s = laplace_transform(f_t, t, s, noconds=True)
G_s = laplace_transform(g_t, t, s, noconds=True)

F_s_func = lambdify(s, F_s, "numpy")
G_s_func = lambdify(s, G_s, "numpy")

s_values = np.linspace(-10, 10, 400)

fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(s_values, np.real(F_s_func(s_values)), color='blue')
axs[0, 0].set_title('Re(F(s))')
axs[0, 1].plot(s_values, np.imag(F_s_func(s_values)), color='red')
axs[0, 1].set_title('Im(F(s))')

axs[1, 0].plot(s_values, np.real(G_s_func(s_values)), color='green')
axs[1, 0].set_title('Re(G(s))')
axs[1, 1].plot(s_values, np.imag(G_s_func(s_values)), color='orange')
axs[1, 1].set_title('Im(G(s))')

fig.suptitle('Real and Imaginary parts of F(s) and G(s)')

plt.show()