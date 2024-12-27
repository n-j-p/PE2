import PE2

def test_fib_gen():
    g = PE2.fib_gen()
    for i in range(10):
        fib = next(g)
    assert fib == 89

def test_prob2_N_89():
    result = PE2.prob2(89)
    assert result == 2 + 8 + 34