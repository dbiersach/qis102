# roots_sympy.py

from multiprocessing import Process, Queue

import numpy as np
import sympy


def complex_formatter(x):
    if np.iscomplexobj(x) and np.imag(x) == 0:
        return f"{np.round(np.real(x), 4)}"
    else:
        return f"{np.round(x, 4)}"


np.set_printoptions(formatter={"complex_kind": complex_formatter})


# Function to solve the equation
def solve_equation(eqn, symbol, queue):
    solutions = sympy.solve(eqn, symbol)
    queue.put(solutions)


# Function to solve with a timeout
def solve_with_timeout(eqn, symbol, timeout=5):
    queue = Queue()
    process = Process(target=solve_equation, args=(eqn, symbol, queue))
    process.start()
    process.join(timeout)

    if process.is_alive():
        process.terminate()
        process.join()
        return None
    else:
        return queue.get()


# Define the unknown variable symbol
x = sympy.symbols("x")


def find_roots(polynomial):
    print(f"Polynomial: {polynomial}")
    roots = solve_with_timeout(polynomial, x)
    if roots is None:
        print("No roots could be found within the timeout period")
    else:
        if not isinstance(roots[0], sympy.Float):
            print("Analytic Roots:")
            for root_num, root_val in enumerate(roots):
                print(f"  Root #{root_num + 1}: {root_val}")
        np_roots = np.array([complex(root.evalf()) for root in roots])
        print(f"Numeric Roots: {np_roots}")
    print()


def main():
    # Define Equation #1
    find_roots(x**4 + x - 1)

    # Define Equation #2
    find_roots(-(x**2) + x ** (3 / 2) + 5 * x - 6)

    # Define Equation #3
    find_roots(x**3.4 + x - 1)


if __name__ == "__main__":
    main()
