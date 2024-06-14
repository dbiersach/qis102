# hero_abilities.py

import numpy as np

n = 1_000_000

a = np.random.randint(1, 7, n)
a = a + np.random.randint(1, 7, n)
a = a + np.random.randint(1, 7, n)

b = np.random.randint(3, 19, n)

print(np.mean(a), np.std(a))
print(np.mean(b), np.std(b))
