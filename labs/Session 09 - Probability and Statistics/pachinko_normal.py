# pachinko_normal.py


from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import scipy
from numba import njit


@njit
def pachinko_normal(num_balls, num_levels):
    np.random.seed(2016)
    balls = np.zeros(num_balls)
    for ball_num in range(num_balls):
        slot = 0
        for _ in range(num_levels):
            slot += -1 if np.random.rand() < 0.5 else 1
        balls[ball_num] = slot // 2
    return balls


def main():
    # Set simulation parameters
    total_balls = 10_000
    total_levels = 10

    # Simulate the pachinko machine
    balls = pachinko_normal(total_balls, total_levels)

    # Calculate the mean number of of balls in each slot
    slots = np.zeros(total_levels + 1)
    first_slot = total_levels // 2
    for ball_num in range(total_balls):
        slot_num = int(first_slot + balls.take(ball_num))
        slots[slot_num] += 1
    slots = slots / total_balls

    # Create an array of slot numbers
    x = np.linspace(-total_levels // 2, total_levels // 2, total_levels + 1)

    # Calculate the expected number of balls in each slot
    mu = np.mean(balls)
    sigma = np.std(balls)

    # Create arrays to hold the values of a perfect normal distribution
    norm_x = np.linspace(-total_levels // 2, total_levels // 2, 100)
    norm_y = scipy.stats.norm(mu, sigma).pdf(norm_x)

    # Plot the results
    plt.figure(Path(__file__).name)
    plt.plot(x, slots, color="blue", linewidth=2, label="Pachinko PDF")
    plt.plot(norm_x, norm_y, color="red", linewidth=2, label="Normal PDF")
    plt.title(
        f"Pachinko vs. Normal PDF ({total_balls:,} balls : {total_levels:,} levels)"
    )
    plt.xlabel("Slot Number")
    plt.ylabel("Probability")
    plt.legend(loc="upper right")
    plt.show()


main()
