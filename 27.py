# Quadratic primes
# Problem 27

# Euler discovered the remarkable quadratic formula:
# n^2 + n + 41
# It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 40^2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.
# The incredible formula  n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, -79 and 1601, is -126479.
# Considering quadratics of the form:
# n^2 + an + b, where |a| < 1000 and |b| < 1000
# where |n| is the modulus/absolute value of n
# e.g. |11| = 11 and |-4| = 4
# Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

# Answer: -59231


def prime_sieve(maximum):
    primes = set(xrange(3, maximum+1, 2))
    primes.add(2)
    for n in xrange(3, int(maximum ** 0.5) + 1, 2):
        if n in primes:
            for m in xrange(n*n, maximum+1, 2*n):
                primes.discard(m)
    return primes

primes = prime_sieve(100000)
not_prime = lambda num: False if num in primes else True


def num_prime(a, b):
    f = lambda n: n * (n+a) + b
    for n in xrange(1000):
        if not_prime(f(n)):
            return n
    return 1000


def main():
    # result, a, b = max((num_prime(a, b), a, b) for a in xrange(-999, 1000, 2) for b in xrange(3, 1000, 2))
    # print result, a, b, a*b
    ta, tb, tn = 0, 0, 0
    for a in xrange(-999, 1000, 2):
        for b in xrange(3, 1000, 2):
            if not_prime(b):
                continue
            n = num_prime(a, b)
            if n > tn:
                ta, tb, tn = a, b, n
    print(ta * tb)


if __name__ == '__main__':
    main()
