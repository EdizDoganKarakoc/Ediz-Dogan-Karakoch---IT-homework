import numpy as np
import matplotlib.pyplot as plt
import random

x = np.linspace(0, 10, random.randint(90, 200))
y = np.sin(x)/x

plt.scatter(x, y, c=x, cmap='Blues_r')
plt.xlabel('Ось х')
plt.ylabel('Ось y')
plt.title('Градиент')
plt.grid(True)
plt.show()