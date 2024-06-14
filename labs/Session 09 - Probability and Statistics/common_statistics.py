# common_statistics.py

import collections

import numpy as np


def mean(s):
    return np.sum(s) / len(s)


def median(s):
    s.sort()
    i = len(s) // 2
    if len(s) % 2 == 1:
        return s[i]
    else:
        return (s[i - 1] + s[i]) / 2


def mode(s):
    c = collections.Counter(s)
    max_c = max(c.values())
    if max_c == 1:
        return None
    else:
        return [k for k, v in c.items() if v == max_c]


def main():
    rng = np.random.default_rng()
    a = rng.integers(low=1, high=100, size=30, endpoint=True)

    print(f"a = {a}")
    print(f"{mean(a) = }")
    print(f"{median(a) = }")
    print(f"{mode(a) = }")


main()
