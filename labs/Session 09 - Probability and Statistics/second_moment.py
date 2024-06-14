# second_moment.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator


def main():
    dice = [4, 6, 8, 10, 12, 20]  # number of sides of die
    magic = np.zeros((len(dice), 21), dtype=float)  # (6x21) magic number 2D matrix
    for idx, sides in enumerate(dice):
        for n in range(len(magic[0])):  # 0 <= n < 21 (# items in 1st row of matrix)
            count = 2 ** (n + 4)  # actual total count of rolls to make
            rolls = np.random.randint(1, sides + 1, count)  # array of random rolls
            var = np.var(rolls)  # variance of random rolls
            magic[idx, n] = (sides - 1) ** 2 / var  # calculate magic number

    # Print the final (largest roll count) magic number for each die
    for idx, sides in enumerate(dice):
        print(f"{sides:3}: {magic[idx,-1]:>8.5f}")

    # Plot the magic number as a function of die sides and count of rolls
    plt.figure(Path(__file__).name)
    x = np.arange(len(magic[idx, :])) + 8  # x-axis domain (minimum of 8 rolls)
    for idx, sides in enumerate(dice):
        plt.plot(x, magic[idx, :], label=f"{sides} sided")

    plt.title("Magic Number (per die sides)")
    plt.xlabel("Number of rolls $(2^x)$")
    plt.ylabel("Magic Number")
    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(2))
    ax.yaxis.set_major_locator(MultipleLocator(1))
    ax.legend(loc="upper right")
    plt.show()


main()
