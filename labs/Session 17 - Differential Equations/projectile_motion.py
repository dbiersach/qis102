# projectile_motion.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle

range = 30  # m
t = np.radians(45)  # 45 degree launch angle
g = 9.81  # m/s^2
v0 = 15  # initial velocity (m/s)

x = np.linspace(0, 40)
y = np.tan(t) * x - (g / (2 * v0**2 * np.cos(t) ** 2)) * x**2

plt.figure(Path(__file__).name)
plt.plot(x, y)
plt.title("Circus Performer Projectile Motion")
plt.xlabel("Distance (m)")
plt.ylabel("Height (m)")
plt.xlim(left=0)
plt.ylim(bottom=0)
ax = plt.gca()
ax.add_patch(Rectangle((27.5, 0), 5, 1, color="red"))
ax.set_aspect("equal")
plt.show()
