#!/usr/bin/env python
from audioop import mul
import gmpy2
import random
import math


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def fermat_factor(n):
    assert n % 2 != 0

    a = gmpy2.isqrt(n)
    b2 = gmpy2.square(a) - n

    while not gmpy2.is_square(b2):
        a += 1
        b2 = gmpy2.square(a) - n

    p = a + gmpy2.isqrt(b2)
    q = a - gmpy2.isqrt(b2)

    return int(p), int(q)


def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi


def get_d(p, q, e):
    # Phi is the totient of n
    phi = (p-1) * (q-1)
    d = multiplicative_inverse(e, phi)
    return d


def decrypt(pk, ciphertext):
    # Unpack the key into its components
    key, n = pk
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    aux = [str(pow(char, key, n)) for char in ciphertext]
    # Return the array of bytes as a string
    plain = [chr(int(char2)) for char2 in aux]
    return ''.join(plain)


if __name__ == "__main__":
    N = 194543069989092070205189872451149402331
    e = 167987920838193759718187925368299723771
    encrypted_msg = "190568463436715256160428577178496619547 152527298467057768983495404402947867435 108898777283556533993662567273504458978 68387833787749222452004657259158314977 49448973860703489046053802062096100079 39054883403023173160204320542206891363 27184219318758100722572910488531834001 139740448572170680116360391831677152430 14544076639926651428274570287177268025 27184219318758100722572910488531834001 59219238142567628177868034944659298678 104095984573218964867640406346989481747 139740448572170680116360391831677152430 14544076639926651428274570287177268025 71259754536916441264022276225437865448 139740448572170680116360391831677152430 155243351795885582845655430890315169647 27184219318758100722572910488531834001 59761741374645051817549478104531903508"

    encrypted_msg = encrypted_msg.split(' ')
    encrypted_msg_int = []
    for letter in encrypted_msg:
        encrypted_msg_int.append(int(letter))

    (p, q) = fermat_factor(N)

    print("p = {}".format(p))
    print("q = {}".format(q))
    
    private = (get_d(p, q, e), N)
    print(private)
    print(" - Your message is: ", decrypt(private, encrypted_msg_int))