# newton_sqrt.py

import numpy as np


def sqrt(x):
    low, high = 0, x
    est = (low + high) / 2
    while np.abs(est**2 - x) > 1e-10:
        if est**2 < x:
            low = est
        else:
            high = est
        est = (low + high) / 2
    return est


def main():
    x = 168923.74
    print(x)
    print(sqrt(x))


main()
