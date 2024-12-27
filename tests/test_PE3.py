import PE3

def test_prime_factors():
    assert list(PE3.prime_factor_generator(13195)) == [5, 7, 13, 29]

def test_prime_sieve():
    assert PE3.primes(0) == []
    assert PE3.primes(3) == [2,]
    assert PE3.primes(4) == [2,3]
    assert PE3.primes(100) == [2, 3, 5, 7, 11, 13, 17, 19, 
                                    23, 29, 31, 37, 
                                    41, 43, 47, 53, 59, 
                                    61, 67, 71, 73, 79, 
                                    83, 89, 97]

def test_prob3():
    assert PE3.prob3(13195) == 29