import numpy as np
import matplotlib.pyplot as plt


A = 2/3
B = -4/3


def inverse_z_transform(A, B, n):
    term1 = A * (0.4)**n * (n >= 0)  
    term2 = B * (0.6)**n * (n >= 0)  
    return term1 + term2


n_values = np.arange(0, 20)


inverse_z_transform_values = inverse_z_transform(A, B, n_values)


plt.stem(n_values, inverse_z_transform_values)
plt.title('Inverse Z-transform of $X(z) = \\frac{6 - 9z^{-1}}{1 - 2.5(z^{-1} + z^{-2})}$')
plt.xlabel('n')
plt.ylabel('$x(n)$')
plt.grid(True)
plt.show()
