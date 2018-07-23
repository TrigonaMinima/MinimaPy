# https://code.activestate.com/recipes/117119-sieve-of-eratosthenes/
# http://stackoverflow.com/q/567222/2650427


def primes():
    """Yields the sequence of prime numbers via the Sieve of Eratosthenes."""

    D = {}  # map composite integers to primes witnessing their compositeness
    q = 2   # first integer to test for primality
    while 1:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1
