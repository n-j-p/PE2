import utils
def mult35(n):
    return filter(lambda x: x % 3 == 0 or x % 5 == 0,
                  range(1, n))
@utils.time
def prob1(n):
    '''Problem 1'''
    return sum(mult35(n))

if __name__ == '__main__':
    prob1(1000)
    