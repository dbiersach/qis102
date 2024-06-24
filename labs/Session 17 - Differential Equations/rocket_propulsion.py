# rocket_propulsion.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Set simulation duration
tf = 5  # final time (secs)
ts = 200  # time steps
dt = tf / ts  # delta time

# Initialize arrays
t = np.zeros(ts)
m = np.zeros(ts)
a = np.zeros(ts)
v = np.zeros(ts)
s = np.zeros(ts)

# Set initial conditions
m[0] = 2.0  # initial mass = 2 kg
a[0] = 0.5  # initial accel = 0.5 m/s^2

# Calculate values at each next time step
# Insert your code here
for i in range(ts - 1):
    t[i + 1] = t[i] + dt
    m[i + 1] = np.exp(-t[i]) + 1
    a[i + 1] = np.exp(-t[i]) / 2
    v[i + 1] = v[i] + m[i] * a[i] * dt
    s[i + 1] = s[i] + v[i] * dt
# Do not edit the remaining code
# Display final distance
print(f"s = {s[-1]:.4f} m")

# Plot values over time
plt.figure(Path(__file__).name)
plt.plot(t, m, label="mass (kg)")
plt.plot(t, a, label="accel (m/s^2)")
plt.plot(t, v, label="velocity (m/s)")
plt.plot(t, s, label="distance (m)")
plt.title("Rocket Propulsion")
plt.xlabel("Seconds")
plt.ylabel("Amplitude")
plt.legend(loc="right")
plt.grid()
plt.show()
