# rsa_demo.py


def extended_euclidean(a, b):
    swapped = False
    if a < b:
        a, b = b, a
        swapped = True
    ca, cb = ((1, 0), (0, 1))
    while b != 0:
        k = int(a // b)
        a, b, ca, cb = (b, a - b * k, (cb), (ca[0] - k * cb[0], ca[1] - k * cb[1]))
    if swapped:
        return ca[1], ca[0]
    else:
        return ca


def power_modulus(b, e, n):
    r = 1
    for i in range(e.bit_length(), -1, -1):
        r = (r * r) % n
        if (e >> i) & 1:
            r = (r * b) % n
    return r


def generate_keys(p, q):
    # Calculate the public modulus (product of two primes)
    n = p * q
    # As p and q are both primes, Euler's totient is simple
    totient = (p - 1) * (q - 1)
    # Set public encryption exponent (a prime number)
    e = 35537
    # Set private encryption exponent
    d = extended_euclidean(e, totient)[0]
    if d < 0:
        d += totient
    # Create a dictionary to hold both keys
    return {"priv": (d, n), "pub": (e, n)}


def encrypt(m, public_key):
    e, n = public_key
    return power_modulus(m, e, n)


def decrypt(m, private_key):
    d, n = private_key
    return power_modulus(m, d, n)


def main():
    # Pick two (normally large random) prime numbers
    p, q = 31337, 31357

    keys = generate_keys(p, q)
    print(f"RSA Encryption Keys: {keys}")

    private_key = keys["priv"]
    public_key = keys["pub"]

    plaintext = "Hi!"
    print(f"Plaintext = {plaintext}")

    b = bytearray(plaintext, encoding="utf-8")
    plaintext_int = int.from_bytes(b, "big")
    print(f"Plaintext as Integer = {plaintext_int}")

    ciphertext_int = encrypt(plaintext_int, private_key)
    print(f"Ciphertext as Integer = {ciphertext_int}")

    plaintext_int = decrypt(ciphertext_int, public_key)
    print(f"Plaintext as Integer = {plaintext_int}")

    b = bytearray(plaintext_int.to_bytes(3, "big"))
    plaintext = b.decode(encoding="utf-8")
    print(f"Plaintext = {plaintext}")


main()
