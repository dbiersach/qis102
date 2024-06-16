# fermat_derivative.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator


def f(x):
    return np.cos(x)


def f_prime_analytic(x):
    return -np.sin(x)


def f_prime_fermat(x, h):
    return (f(x + h) - f(x)) / h


def f_prime_centered(x, h):
    return (f(x + h) - f(x - h)) / (2 * h)


def main():
    a, b = -4 * np.pi, 4 * np.pi
    n = 500
    h = (b - a) / n
    x = np.linspace(a, b, n)

    y = f(x)
    y_prime_actual = f_prime_analytic(x)
    y_prime_fermat = f_prime_fermat(x, h)
    y_prime_centered = f_prime_centered(x, h)

    print(f"Fermat Error   : {sum((y_prime_actual-y_prime_fermat)**2):>9.7f}")
    print(f"Centered Error : {sum((y_prime_actual-y_prime_centered)**2):>9.7f}")

    plt.figure(Path(__file__).name)
    plt.plot(x, y, label=r"$y=\cos{x}$")
    plt.plot(x, y_prime_centered, label=r"$\frac{dy}{dx}=-\sin{x}$")

    plt.title("Fermat's Difference Quotient")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.axhline(0, color="black", linestyle="-")
    plt.axvline(0, color="black", linestyle="-")

    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(2))
    ax.yaxis.set_major_locator(MultipleLocator(0.2))
    ax.legend(loc="upper right")

    plt.show()


main()
