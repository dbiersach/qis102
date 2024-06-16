# eqn1_roots.py

import numpy as np
from numpy.polynomial import Polynomial
from scipy.optimize import fsolve


def complex_formatter(x):
    if np.iscomplexobj(x) and np.imag(x) == 0:
        return f"{np.round(np.real(x), 4)}"
    else:
        return f"{np.round(x, 4)}"


np.set_printoptions(formatter={"complex_kind": complex_formatter})


def f(x):
    return x**4 + x - 1


print("Roots of f(x)")
print("Via scipy")
# SciPy fsolve() only shows two real roots
print(fsolve(f, -1.5))
print(fsolve(f, 0.5))
print("Via numpy")
# It turns out f(x) truly has FOUR roots:
#  - Two distinct real roots
#  - Two complex roots (a conjugate pair)
p = Polynomial([-1, 1, 0, 0, 1])
roots = p.roots()
print(roots)
print("Valid roots")
print(roots[np.isclose(f(roots), 0)])
