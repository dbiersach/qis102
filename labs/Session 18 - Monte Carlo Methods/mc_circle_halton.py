# mc_circle_halton.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from numba import float64, int64, vectorize


@vectorize([float64(int64, int64)], nopython=True)
def halton(n, p):
    h, f = 0, 1
    while n > 0:
        f = f / p
        h += (n % p) * f
        n = int(n / p)
    return h


def main():
    dots = 25_600

    x = (1 - halton(np.arange(dots), 2)) * 2 - 1
    y = (1 - halton(np.arange(dots), 3)) * 2 - 1

    d = x**2 + y**2

    x_in = x[d <= 1.0]
    y_in = y[d <= 1.0]
    x_out = x[d > 1.0]
    y_out = y[d > 1.0]

    act = np.pi
    est = np.count_nonzero(d <= 1.0) / dots * 4
    err = np.abs((est - act) / act)

    print(f"dots = {dots:,}")
    print(f"act = {act:.6f}")
    print(f"est = {est:.6f}")
    print(f"err = {err:.5%}")

    plt.figure(Path(__file__).name, figsize=(10, 8))
    plt.scatter(x_in, y_in, color="red", marker=".", s=0.5)
    plt.scatter(x_out, y_out, color="blue", marker=".", s=0.5)
    plt.gca().set_aspect("equal")
    plt.tight_layout()
    plt.show()


main()
