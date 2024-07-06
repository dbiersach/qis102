# mc_std_normal.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from numba import float64, vectorize


def f(x):
    # Standard Normal PDF
    return 1.0 / np.sqrt(2.0 * np.pi) * np.exp(-np.power(x, 2) / 2.0)


@vectorize([float64(float64, float64)], nopython=True)
def halton(n, p):
    h, f = 0, 1
    while n > 0:
        f = f / p
        h += (n % p) * f
        n = int(n / p)
    return h


def main():
    dots = 30_000

    # Sample area is (-1 to 1)x(0 to 0.5)
    x = (1 - halton(np.arange(dots), 2)) * 2.0 - 1.0
    y = (1 - halton(np.arange(dots), 3)) * 0.5

    d = y - f(x)

    x_in = x[d <= 0.0]
    y_in = y[d <= 0.0]
    x_out = x[d > 0.0]
    y_out = y[d > 0.0]

    est_area = np.count_nonzero(d <= 0.0) / dots
    act_area = 0.682689492
    err = np.abs((est_area - act_area) / act_area)

    print(f"dots = {dots:,}")
    print(f"act = {act_area:.6f}")
    print(f"est = {est_area:.6f}")
    print(f"err = {err:.5%}")

    act_x = np.linspace(-4, 4, 100)
    act_y = f(act_x)

    plt.figure(Path(__file__).name, figsize=(10, 8))
    plt.scatter(x_in, y_in, color="red", marker=".", s=0.5)
    plt.scatter(x_out, y_out, color="blue", marker=".", s=0.5)
    plt.plot(
        act_x, act_y, color="green", label=r"$\frac{1}{\sqrt{2\pi}}e^{\frac{-x^2}{2}}$"
    )
    plt.title("Standard Normal CDF")
    plt.axhline(0, color="gray")
    plt.axvline(0, color="gray")
    plt.xlim(-4.0, 4.0)
    plt.ylim(-0.1, 0.6)
    plt.legend(loc="upper right", fontsize="12")
    plt.tight_layout()
    plt.show()


main()
