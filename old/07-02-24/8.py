import numpy as np
import matplotlib.pyplot as plt


A = 3/4
B = 1/2
C = 1/4


def inverse_z_transform(A, B, C, n):
    term1 = A * (2**n) * (n >= 0)  
    term2 = B * (-1)**n * (n >= 0)  
    term3 = C * (1**n) * (n >= 0)  
    return term1 + term2 + term3


n_values = np.arange(0, 20)


inverse_z_transform_values = inverse_z_transform(A, B, C, n_values)


plt.stem(n_values, inverse_z_transform_values)
plt.title('Inverse Z-transform of $X(z) = \\frac{1}{6 - 5z^{-1} + z^{-2}} \\left(\\frac{4z}{4z-1} - z^{-1} + 5z^{-1}\\right)$')
plt.xlabel('n')
plt.ylabel('$x(n)$')
plt.grid(True)
plt.show()