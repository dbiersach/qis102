# eqn1_plot.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return x**4 + x - 1


plt.figure(Path(__file__).name)
x = np.linspace(-1.5, 1.5, 100)
plt.plot(x, f(x))
plt.title("$f(x)=x^4+x-1$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axhline(0, color="black")
plt.grid("on")
plt.show()
