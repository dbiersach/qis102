# mc_high_dimensions.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import sympy
from matplotlib.ticker import AutoMinorLocator, MultipleLocator
from numba import float64, vectorize
from scipy.signal import find_peaks
from scipy.special import gamma


@vectorize([float64(float64, float64)], nopython=True)
def halton(n, p):
    h, f = 0, 1
    while n > 0:
        f = f / p
        h += (n % p) * f
        n = int(n / p)
    return h


def main():
    dots = 6_250_000

    dimensions = 13
    d = np.zeros(dots)
    est = np.zeros(dimensions)
    est[0] = 1  # By definition
    est[1] = 2  # The 1-D interval [-1,1] has length 2

    for dim in np.arange(1, dimensions):
        print(f"Calculating the volume of a unit {dim:>2}-ball . . .")
        v = (1 - halton(np.arange(dots), sympy.prime(dim))) * 2 - 1
        d += v**2
        est[dim] = np.count_nonzero(d <= 1.0) / dots * 2**dim

    act_x = np.linspace(0, dimensions - 1, 1000)
    act_y = np.power(np.pi, act_x / 2) / gamma(act_x / 2 + 1)
    m = find_peaks(act_y)[0][0]
    print(f"max dim = {act_x[m]:.6f}")
    print(f"max vol = {act_y[m]:.6f}")

    plt.figure(Path(__file__).name)
    plt.plot(np.arange(dimensions), est, color="blue", label="Estimated")
    plt.plot(act_x, act_y, color="red", label="Actual")
    plt.scatter(act_x[m], act_y[m], marker="o", color="green")
    plt.vlines(act_x[m], 0, act_y[m], color="green")
    plt.title("Volume of n-Dimensional Hyperspheres")
    plt.xlabel("Dimension")
    plt.ylabel("Volume")
    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.xaxis.set_minor_locator(MultipleLocator(0.5))
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.legend(loc="upper right")
    ax.grid("on")
    plt.show()


main()
