# plot_superposition.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 4 * np.pi, 1000)
r = 7 + 7 * np.sin(11 * t) * np.cos(5 * t)

plt.figure(Path(__file__).name)
plt.subplot(projection="polar")
plt.plot(t, r, color="black")
plt.show()
