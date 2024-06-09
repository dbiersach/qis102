# basel_series.py

import numpy as np

n = np.arange(1, 50_000)

y1 = np.sum(1 / n)
y2 = np.sum(1 / n**2)

print(f"{y1 = }")
print(f"{y2 = }")
print(f"{np.sqrt(6 * y2) = }")
