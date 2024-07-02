import numpy as np
import matplotlib.pyplot as plt



A = -1
B = 2


def inverse_z_transform(A, B, n):
    term1 = A * (0.5)**n * (n >= 0)  
    term2 = B * 2**n * (n >= 0)  
    return term1 + term2


n_values = np.arange(0, 20)


inverse_z_transform_values = inverse_z_transform(A, B, n_values)


plt.stem(n_values, inverse_z_transform_values)
plt.title('Inverse Z-transform of $X(z) = \\frac{2z}{2z-1}$')
plt.xlabel('n')
plt.ylabel('$x(n)$')
plt.grid(True)
plt.show()