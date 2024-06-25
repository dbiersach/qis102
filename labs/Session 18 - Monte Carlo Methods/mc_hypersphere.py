# mc_hypersphere.py

import numpy as np
from numba import float64, vectorize


@vectorize([float64(float64, float64)], nopython=True)
def halton(n, p):
    h, f = 0, 1
    while n > 0:
        f = f / p
        h += (n % p) * f
        n = int(n / p)
    return h


dots = 6_250_000

x = (1 - halton(np.arange(dots), 2)) * 2 - 1
y = (1 - halton(np.arange(dots), 3)) * 2 - 1
z = (1 - halton(np.arange(dots), 5)) * 2 - 1
w = (1 - halton(np.arange(dots), 7)) * 2 - 1

d = x**2 + y**2 + z**2 + w**2

act = np.pi**2 / 2
est = np.count_nonzero(d <= 1.0) / dots * 16
err = np.abs((est - act) / act)

print(f"dots = {dots:,}")
print(f"act = {act:.6f}")
print(f"est = {est:.6f}")
print(f"err = {err:.5%}")
