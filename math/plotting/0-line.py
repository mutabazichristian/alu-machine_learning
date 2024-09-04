#!usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3
x = np.arange(0, 11)

plt.plot(x, y, marker='.', color='red')

# Some modifications
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Graph')

plt.show()
