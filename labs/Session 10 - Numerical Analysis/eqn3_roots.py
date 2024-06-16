# eqn3_roots.py

import numpy as np
from scipy.optimize import fsolve


def complex_formatter(x):
    if np.iscomplexobj(x) and np.imag(x) == 0:
        return f"{np.round(np.real(x), 4)}"
    else:
        return f"{np.round(x, 4)}"


np.set_printoptions(formatter={"complex_kind": complex_formatter})


def h(x):
    return x**3.4 + x - 1


print("Roots of h(x)")
print("Via scipy")
print(fsolve(h, 1))
# The fundamental theorem of algebra is not applicable
# because the leading exponent is not an integer
# It turns out h(x) truly has THREE roots:
# - One real root
# - Two complex roots (two conjugate pairs)
print("Via numpy")
roots = np.roots([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, -5, 10, -10, 5, -1])
print(roots)
# The other reported complex roots come in
# because we artificially raised h(x) to the power of 5
print("Valid roots")
print(roots[np.isclose(h(roots), 0)])
