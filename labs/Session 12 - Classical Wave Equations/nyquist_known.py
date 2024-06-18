# nyquist_known.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator

a, b, n = (0, 20, 640)
x = np.linspace(a, b, n + 1)
y = np.sin(4 / 5 * np.pi * x)

plt.figure(Path(__file__).name)
# fmt: off
plt.plot(x, y, color="blue", marker="o", markersize=2,
    markerfacecolor="red", markeredgecolor="red")
# fmt: on
plt.title(rf"$y=\sin\left(\frac{{4}}{{5}}\pi x\right)$ at {n:,} samples")
plt.xlabel("x")
plt.ylabel("y")
plt.ylim(-1.1, 1.2)
plt.axhline(y=0, color="lightgray")
ax = plt.gca()
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
plt.show()
