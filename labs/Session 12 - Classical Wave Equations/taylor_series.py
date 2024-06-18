# taylor_series.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import sympy


def main():
    # Plot exact y = cos(x)
    x = np.linspace(0, 2 * np.pi, 1000)
    plt.figure(Path(__file__).name)
    plt.plot(x, np.cos(x), label="Exact")

    # Plot Newton's Expansion for cos(x)
    # fmt: off
    plt.plot(x, 1 - (1 / 2) * np.power(x, 2) / 2  + (1 / 24) * np.power(x, 4)
        - (1 / 720) * np.power(x, 6) + (1 / 362880) * np.power(x, 9),
        label="Newton (5 terms)",
    )
    # fmt: on

    # Plot Taylor Series for cos(x)
    num_terms_taylor = 5
    xs = sympy.symbols("x")
    poly = sympy.cos(xs).series(xs, 0, num_terms_taylor).removeO()
    eqn = sympy.lambdify(xs, poly.as_expr(), modules="numpy")
    print(f"Taylor Series for cos(x) = {poly}")
    plt.plot(x, eqn(x), label=f"Taylor ({num_terms_taylor} terms)")

    # Plot Euler's Method for d[cos(x)] = -sin(x)
    num_terms_euler = 20
    xm = np.linspace(0, 2 * np.pi, num_terms_euler)
    ym = np.zeros(num_terms_euler)
    dx = xm[1] - xm[0]
    ym[0] = np.cos(0)
    for i in range(1, len(xm)):
        ym[i] = ym[i - 1] - np.sin(xm[i - 1]) * dx
    plt.plot(xm, ym, label=f"Euler ({num_terms_euler} terms)")

    plt.title(r"Series Comparison for $y = \cos(x)$")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.ylim(-1.1, 1.1)
    plt.axhline(y=0.0, color="lightgray", zorder=-2)
    plt.legend(loc="lower left")
    plt.show()


main()
