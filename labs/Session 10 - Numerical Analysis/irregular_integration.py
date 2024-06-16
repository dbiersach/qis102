# irregular_integration.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import cumulative_simpson


def y(theta):
    return np.sin(theta) ** 2


n = 50  # Number of samples

# Generate 'n' random radians
np.random.seed(2022)
theta = np.sort(np.pi * np.random.rand(n))
# Take samples at those angles
y_samples = y(theta)

# Compute the cumulative integral using Simpson's rule
# of the samples taken at randomly distributed angles
area_dscr = cumulative_simpson(y_samples, x=theta)

# Compare discrete vs. analytic integral value
print(f"Discrete Integral: {area_dscr[-1]:0.4f}")
print(f"Analytic Integral: {np.pi/2:0.4f}")

# Plot discrete (sampled) data
plt.figure(Path(__file__).name)
plt.scatter(theta, y_samples, color="r", label=f"$({n})$ samples")
# Overlay smooth f(x)
theta = np.linspace(0, np.pi, 1000)
plt.plot(theta, y(theta), label=r"$\sin^2\theta$")
plt.title("Cumulative Integration of Random Samples")
plt.xlabel(r"$\theta$ (radians)")
plt.ylabel("Amplitude")
plt.legend()
plt.show()
