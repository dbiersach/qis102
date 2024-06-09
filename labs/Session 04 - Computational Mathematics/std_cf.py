# std_cf.py

import math

MAX_TERMS = 20


def normalize_cf(cf):
    while len(cf) > 2 and cf[-1] == 1 and cf[-2] != 1:
        cf[int(-2)] += 1
        cf.pop(-1)
    return cf


def encode_cf(x):
    cf: list[int] = []
    while len(cf) < MAX_TERMS:
        cf.append(int(x))
        x = x - int(x)
        if x < 1e-11:
            break
        x = 1 / x
    return normalize_cf(cf)


def decode_cf(cf):
    h_n, k_n = 0, 0
    b_1, h_1, k_1 = 1, 1, 0
    h_2, k_2 = 0, 1
    for term in cf:
        a_n, b_n = term, 1
        h_n = a_n * h_1 + b_1 * h_2
        k_n = a_n * k_1 + b_1 * k_2
        b_1 = b_n
        h_1, h_2 = h_n, h_1
        k_1, k_2 = k_n, k_1
    return h_n / k_n


def eval_cf(x):
    cf = encode_cf(x)
    x2 = decode_cf(cf)
    print(f"{x} -> {cf} -> {x2}")


def main():
    eval_cf(3.245)
    eval_cf(math.sqrt(2))
    eval_cf(math.sqrt(113))
    eval_cf(math.e)

    golden_ratio = (1 + math.sqrt(5)) / 2
    eval_cf(golden_ratio)


main()
