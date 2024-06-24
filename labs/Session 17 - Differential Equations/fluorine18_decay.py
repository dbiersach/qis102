# fluorine18_decay.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Set simulation duration
tf = 12  # final time (hours)
ts = 100  # time steps
dt = tf / ts  # delta time

# Initialize arrays
t = np.zeros(ts)
n = np.zeros(ts)

# Set initial conditions
n[0] = 100  # initial 100% concentration
tau = 1.829  # half-life (hours)

for i in range(ts - 1):
    t[i + 1] = t[i] + dt
    n[i + 1] = n[i] - n[i] / tau * dt

plt.figure(Path(__file__).name)
plt.plot(t, n)
plt.title("Fluorine-18 Decay")
plt.xlabel("Time (hours)")
plt.ylabel("% Concentration")
plt.show()
