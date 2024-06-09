# plot_circle.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

r = 250
t = np.linspace(0, 2 * np.pi, 1000)
x = r * np.cos(t)
y = r * np.sin(t)

plt.figure(Path(__file__).name)
plt.plot(x, y)
plt.grid("on")
plt.gca().set_aspect("equal")
plt.show()
