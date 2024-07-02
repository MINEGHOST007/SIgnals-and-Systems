import numpy as np
import matplotlib.pyplot as plt
import sympy

t, s = sympy.symbols('t s')
def L(f):
    return sympy.laplace_transform(f, t, s, noconds=True)

y1 = t**2
lp1 = L(y1)

lp1_func = sympy.lambdify(s, lp1, 'numpy')
s_values = np.linspace(0, 10, 100)

lp1_values = lp1_func(s_values)

plt.plot(s_values, lp1_values)
plt.xlabel('s')
plt.ylabel('Laplace Transform')
plt.title('Laplace Transform of t^2')
plt.grid(True)
plt.show()