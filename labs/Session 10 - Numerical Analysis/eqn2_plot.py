# eqn2_plot.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator


def g(x):
    return -(x**2) + x ** (3 / 2) + 5 * x - 6


plt.figure(Path(__file__).name)
x = np.linspace(0, 10, 100)
plt.plot(x, g(x))
plt.title(r"$g(x)=-x^2+x^\frac{3}{2}+5x-6$")
plt.xlabel("x")
plt.ylabel("g(x)")
plt.axhline(0, color="black")
plt.gca().xaxis.set_major_locator(MultipleLocator(1))
plt.grid("on")
plt.show()
