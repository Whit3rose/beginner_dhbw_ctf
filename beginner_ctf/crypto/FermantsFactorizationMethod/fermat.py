#!/usr/bin/env python
import gmpy2

N = 123731907061228644336839301661400552447

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

if __name__ == "__main__":
    (p, q) = fermat_factor(N)

    print("p = {}".format(p))
    print("q = {}".format(q))