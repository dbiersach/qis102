# plot_rose_curves.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 4 * np.pi, 1000)
r1 = 4 + 4 * np.cos(4 * t)
r2 = 3 + 3 * np.cos(4 * t + np.pi)
r3 = 5 + 5 * np.cos(3 / 2 * t)

plt.figure(Path(__file__).name)
plt.subplot(projection="polar")
plt.plot(t, r1)
plt.plot(t, r2)
plt.plot(t, r3)
plt.show()
