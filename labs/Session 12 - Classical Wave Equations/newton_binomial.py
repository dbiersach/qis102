# newton_binomial.py


from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from sympy import Float, Number, lambdify, symbols


def expr_to_str(expr, num_digits):
    # Returns a string representation of the given polynomial expression
    # rounding each coefficient to fractional part with num_digits precision
    return expr.xreplace(
        {
            n.evalf(): n if isinstance(n, int) else Float(n, num_digits)
            for n in expr.atoms(Number)
        }
    )


def calc_coeff(a, b, r, n):
    # Returns the coefficient for the nth term in the Binomial expansion of (a+b)^r
    coeff = 1.0
    for m in range(n):
        coeff = coeff * (r - m) / (m + 1)
    coeff = coeff * pow(a, r - n)
    coeff = coeff * pow(b, n)
    return coeff


def binomial_expand(a, b, c, r, max_t):
    # Returns a tuple containing the Binomial Expansion of (a+b*x^c)^r
    # to max_t terms as a Sympy Polynomial in x along with
    # a callable Numpy expression for that expansion
    x = symbols("x")
    poly = 0.0
    for t in range(max_t):
        # Append this term (as a symbolic expression in x)
        # to the growing polynomial of max_t terms
        poly += calc_coeff(a, b, r, t) * x ** (c * t)
    return poly, lambdify(x, poly.as_expr(), modules="numpy")


def main():
    x = np.linspace(0, 10, 1000)

    plt.figure(Path(__file__).name)
    plt.plot(x, 1 / np.power(2 * np.power(x, 2) + 7, 2 / 3), label="Exact")

    print(f"{'Terms':>5}   Binomial Expansion")
    for t in range(2, 8):
        # Use Newton's Binomial Theorem to expand (2x^2+7)^(-2/3) to 't' terms
        eqn = binomial_expand(7, 2, 2, -2 / 3, t)
        print(f"{t:>5} = {expr_to_str(eqn[0], 5)}")
        # Evaluate the symbolic expression across the domain x=[0, 10]
        plt.plot(x, np.array(list(map(eqn[1], x))), label=f"{t} terms")

    plt.title(r"Binomial Expansion of $y=(2x^2+7)^{-2/3}$")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.ylim(0, 0.3)
    plt.legend(loc="upper right")
    plt.show()


main()
