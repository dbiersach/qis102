# simple_pendulum.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Set simulation duration
tf = 10  # final time (seconds)
ts = 500  # time steps
dt = tf / ts  # delta time

# Initialize arrays
t = np.zeros(ts)
omega = np.zeros(ts)
theta = np.zeros(ts)

# Set initial conditions
theta[0] = np.deg2rad(45)
g = 9.81  # gravity (m/s^2)
length = 1.0  # pendulum length (m)

# Calculate omega and theta at each next time step
for i in range(ts - 1):
    t[i + 1] = t[i] + dt
    omega[i + 1] = omega[i] - g / length * np.sin(theta[i]) * dt
    theta[i + 1] = theta[i] + omega[i] * dt

# Plot omega and theta over time
plt.figure(Path(__file__).name)
(plot1,) = plt.plot(t, theta, lw=2)
(plot2,) = plt.plot(t, omega, lw=2)
plt.title("Simple Pendulum (Euler Method)")
plt.xlabel("Time (sec)")
plt.ylabel(r"Angular Displacement $\theta$ (rad)")
plt.twinx()
plt.ylabel(r"Angular Velocity $\omega$ (rad/s)")
legend_lines = [plot1, plot2]
legend_labels = [r"$\theta$", r"$\omega$"]
plt.legend(legend_lines, legend_labels)
plt.grid(True)
plt.show()
