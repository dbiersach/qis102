# eqn2_roots.py

import numpy as np
from scipy.optimize import fsolve


def complex_formatter(x):
    if np.iscomplexobj(x) and np.imag(x) == 0:
        return f"{np.round(np.real(x), 4)}"
    else:
        return f"{np.round(x, 4)}"


np.set_printoptions(formatter={"complex_kind": complex_formatter})


def g(x):
    return -(x**2) + x ** (3 / 2) + 5 * x - 6


print("Roots of g(x)")
print("Via scipy")
print(fsolve(g, 1))
print(fsolve(g, 6))
print("Via numpy")
# We can't use the original equation with Numpy roots()
# since the there is a non-integer exponent
# But g(x) only has two distinct real roots!
roots = np.roots([1, -11, 37, -60, 36])
print(roots)
# The other two reported (complex roots) slipped in
# because we artificially squared g(x)
print("Valid roots")
print(roots[np.isclose(g(roots), 0)])
