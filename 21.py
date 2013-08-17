# Amicable numbers
# Problem 21

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.

# Answer: 31626


def d(num):
    if num == 1:
        return 1
    dsum = 1
    sqrt = int(num**0.5)
    for n in xrange(2, sqrt + 1):
        if num % n == 0:
            dsum = dsum + n + num//n
    if sqrt * sqrt == num:
        dsum -= sqrt
    return dsum

if __name__ == '__main__':
    amicable_sum = 0
    for n in xrange(1, 10000):
        dn = d(n)
        if d(dn) == n and dn != n:
            amicable_sum += n
    print(amicable_sum)
