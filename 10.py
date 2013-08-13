# Summation of primes
# Problem 10

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

# Answer: 142913828922

from math import sqrt


def prime_sieve(maximum):
    sieve = [False for n in range(maximum+1)]
    sieve[0] = sieve[1] = True
    for n in range(4, maximum+1, 2):
        sieve[n] = True
    for n in range(3, int(sqrt(maximum)) + 1, 2):
        if not sieve[n]:
            for m in range(n*n, maximum+1, 2*n):
                sieve[m] = True
    return sieve

if __name__ == '__main__':
    summation = 0
    sieve = prime_sieve(2000000)
    for n in range(len(sieve)):
        if not sieve[n]:
            summation += n
    print(summation)
