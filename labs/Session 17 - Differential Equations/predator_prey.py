# predator_prey.py

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from scipy.integrate import solve_ivp


def model(time, state_vector, alpha, beta, delta, gamma):
    pred, prey = state_vector
    d_prey = alpha * prey - beta * prey * pred
    d_pred = delta * prey * pred - gamma * pred
    return d_pred, d_prey


def main():
    # Set model duration (dimensionless)
    t_0, t_f = 0, 20

    # Set simulation constants
    alpha = 2.0  # Prey birth rate
    beta = 1.1  # Prey death rate
    delta = 1.0  # Pred birth rate
    gamma = 0.9  # Pred death rate

    # Set initial conditions (% of population)
    pred_0, prey_0 = 0.5, 1.0

    # fmt: off
    sol = solve_ivp(model, (t_0, t_f), [pred_0, prey_0],
        max_step=0.01, args=(alpha, beta, delta, gamma))
    # fmt: on

    # Retrieve results of the solution
    t = sol.t
    pred, prey = sol.y * 100  # Convert to %

    # Plot Predator vs Prey populations over time
    plt.figure(Path(__file__).name)
    plt.plot(t, pred, label="predator", color="red", linewidth=2)
    plt.plot(t, prey, label="prey", color="blue", linewidth=2)
    plt.title("Predator-Prey Model (Lotka-Volterra)")
    plt.xlabel("Time")
    plt.ylabel("% Population")
    ax = plt.gca()
    ax.xaxis.set_major_locator(MultipleLocator(5))
    ax.xaxis.set_minor_locator(MultipleLocator(1))
    ax.yaxis.set_major_locator(MultipleLocator(50))
    ax.yaxis.set_minor_locator(MultipleLocator(10))
    ax.legend(loc="upper right")
    plt.show()


main()
