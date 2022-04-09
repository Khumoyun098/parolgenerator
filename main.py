# This is a sample Python script.


"""
    password generator
"""

import random
from string import ascii_letters


def gen_pass(length: int=20, count: int=0):
    numbers = "1234567890"
    symbols = "!@#$%^&*()+="
    letters = ascii_letters

    chars = numbers+symbols+letters
    passwords = []

    for i in range(count+1):
        password = ""
        for j in range(length):
            password += random.choice(chars)
        passwords.append(password)

    return passwords
