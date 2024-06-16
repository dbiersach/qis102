# eqn3_plot.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def h(x):
    return x**3.4 + x - 1


plt.figure(Path(__file__).name)
x = np.linspace(-2, 2, 100)
# Notice even though x ranges from -2 to 2,
# the plot doesn't show any x values to the
# left of zero because h(x) is complex for x < 0
plt.plot(x, h(x))
plt.title("$h(x)=x^{3.4}+x-1$")
plt.xlabel("x")
plt.ylabel("h(x)")
plt.axhline(0, color="black")
plt.grid("on")
plt.show()
