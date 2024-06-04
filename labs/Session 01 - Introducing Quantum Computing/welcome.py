# welcome.py

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 500)
f_top = np.sqrt(1 - (np.abs(x) - 1) ** 2)
f_bottom = np.arccos(1 - np.abs(x)) - np.pi

plt.plot(x, f_top, color="red")
plt.plot(x, f_bottom, color="red")
plt.xlim(-3.5, 3.5)
plt.ylim(-3.5, 1.5)
plt.title("Welcome to QIS102")
plt.show()
