import utils
import itertools as it

def fib_gen():
    dlast = 1
    last = 1
    while True:
        yield last
        nxt = dlast + last
        dlast = last
        last = nxt

@utils.time
def prob2(N = 4 * 10**6):
    '''Problem 2'''
    terms = it.takewhile(lambda x: x <= N,
                         fib_gen())
    return sum(filter(lambda x: x % 2 == 0,
                      terms))

if __name__ == '__main__':
    prob2()