# euler_gamma.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def factorial_recursive(n):
    if n == 0:
        return 1
    else:
        return int(n) * factorial_recursive(n - 1)


def f(x, s):
    try:
        return np.power(x, s - 1) * np.exp(-x)
    except ZeroDivisionError:
        return 0


def simpsons_rule(func, s, a, b, intervals):
    dx, area = (b - a) / intervals, func(a, s) + func(b, s)
    for i in range(1, intervals):
        area += func(a + i * dx, s) * (2 * (i % 2 + 1))
    return dx / 3 * area


def euler_gamma(s):
    return simpsons_rule(f, s, 0, int(1e3), int(1e5))


def factorial_gamma(x):
    return np.round(euler_gamma(x + 1), 5)


def main(zoom):
    xa = np.linspace(0, 5, 100)
    n = [factorial_recursive(i) for i in range(6)]

    plt.figure(Path(__file__).name)
    plt.plot(xa, factorial_gamma(xa), label=r"$\Gamma \left( x + 1 \right)$")
    plt.plot(range(len(n)), n, color="red", marker="o", label="$n!$")
    plt.title("Factorial Via Euler's Gamma Function")
    plt.xlabel("x")
    plt.ylabel("Factorial (x)")
    if zoom:
        plt.xlim(0, 2.1)
        plt.ylim(0.5, 2.1)
    else:
        plt.xlim(0, 5.1)
    plt.legend(loc="upper left")
    plt.grid("on")
    plt.show()


main(zoom=True)
