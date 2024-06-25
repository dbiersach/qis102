# mc_circle_grid.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def main():
    side_dots = 320
    total_dots = side_dots**2  # 102,400

    x = np.linspace(-1, 1, side_dots)
    y = np.linspace(-1, 1, side_dots)

    xv, yv = np.meshgrid(x, y)
    x = xv.flatten()
    y = yv.flatten()

    d = x**2 + y**2

    x_in = x[d <= 1.0]
    y_in = y[d <= 1.0]
    x_out = x[d > 1.0]
    y_out = y[d > 1.0]

    act = np.pi
    est = 4 * np.count_nonzero(d <= 1.0) / total_dots
    err = np.abs((est - act) / act)

    print(f"dots = {total_dots:,}")
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
