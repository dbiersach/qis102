# aes_demo.py

import os

import aes


def main():
    # The secret key is 16 bytes long
    secret_key = os.urandom(16)
    print(f"Secret key = {bytearray(secret_key).hex()}")

    plaintext = b"Attack at dawn"
    print(f"{plaintext.decode('ascii')}")
    print("plaintext = ")
    print([f"0x{b:02x}" for b in bytearray(plaintext)], sep=", ")

    # The random initialization vector (iv) ensures the same value
    # encrypted multiple times, even with the same secret key,
    # will not always result in the same encrypted value
    # Note: The iv is sent along with the ciphertext to the receiver
    iv = os.urandom(16)

    ciphertext = aes.AES(secret_key).encrypt_ctr(plaintext, iv)
    print("ciphertext =")
    print([f"0x{b:02x}" for b in bytearray(ciphertext)], sep=", ")

    plaintext = aes.AES(secret_key).decrypt_ctr(ciphertext, iv)
    print("plaintext = ")
    print([f"0x{b:02x}" for b in bytearray(plaintext)], sep=", ")
    print(f"{plaintext.decode('ascii')}")


main()
