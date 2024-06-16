# oscillating_integrand.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

a, b = 0, 5000


def f(x):
    return np.cos(x)


def F(x):
    return np.sin(x)


plt.switch_backend("TkAgg")
plt.figure(Path(__file__).name)
x = np.linspace(a, b, 1000)
plt.plot(x, f(x))
plt.title(r"$f(x)=\cos{x}$")
plt.xlabel("x")
plt.ylabel("f(x)")
fig_manager = plt.get_current_fig_manager()
fig_manager.window.state("zoomed")
plt.show()

# scipy.quad()'s default limit of 50 subintervals may fail
# for oscillatory integrands evaluated over large intervals
first_estimate = quad(np.cos, a, b, full_output=True)[0]
print(f"{ first_estimate = :.6f}")

# We can improve scipy.quad()'s adaptive quadrature
# by specifying a greater subinterval limit
second_estimate = quad(np.cos, a, b, full_output=True, limit=1000)[0]
print(f"{second_estimate = :.6f}")

# Compare these estimates to the exact analytic integral
print(f"{    F(b) - F(a) = :.6f}")
