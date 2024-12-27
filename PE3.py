import utils
import math

def divisor_generator(n):
    raise NotImplementedError
    if n % 2 == 0:
        yield n
    if n % 3 == 0:
        yield n
    
    sqrt_n = int(math.sqrt(n))
    k = 1
    m = 6*k - 1
    while m <= sqrt_n:
        if n % m == 0:
            yield m
        m += 2 # i.e. 6k + 1
        if m > sqrt_n:
            return
        if n % m == 0:
            yield m
        k += 1
        m = 6*k -1

def primes(n):
    '''Returns list of prime numbers less than n.'''
    if n < 3:
        return []
    i_sqrt_n = int(math.sqrt(n))
    sieve = list(range(n))
    sieve[1] = 0
    p = 2
    while p <= i_sqrt_n:
        a = 2
        while a*p < n:
            sieve[a*p] = 0
            a += 1
        nxt_p = p + 1
        while sieve[nxt_p] == 0:
            nxt_p += 1
        p = nxt_p
    return list(filter(lambda x: x != 0,
                       sieve))

def prime_factor_generator(n):
    i_sqrt_n = int(math.sqrt(n))
    primes_n = primes(i_sqrt_n)
    for p in primes_n:
        if n % p == 0:
            yield p
@utils.time
def prob3(n):
    '''Problem 3'''
    # Largest prime factor of n
    for p in prime_factor_generator(n):
        pass
    return p

if __name__ == '__main__':
    prob3(600851475143)