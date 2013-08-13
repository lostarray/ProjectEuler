# Smallest multiple
# Problem 5

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Answer: 232792560


def gcd(x, y):
    while y > 0:
        x, y = y, x % y
    return x


def lcm(x, y):
    return x * y / gcd(x, y)


def smallest_multiple(start, end):
    p = range(start, end + 1)
    res = 1
    for elem in p:
        res = lcm(res, elem)
    return res


if __name__ == '__main__':
    print(smallest_multiple(1, 20))
