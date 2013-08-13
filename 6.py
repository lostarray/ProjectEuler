# Sum square difference
# Problem 6

# The sum of the squares of the first ten natural numbers is,
#     1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#     (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# Answer: 25164150


def sum_of_square(n):
    res = 0
    for i in range(1, n+1):
        res += i * i
    return res


def square_of_sum(n):
    s = (1 + n) * n / 2
    return s * s


if __name__ == '__main__':
    res = square_of_sum(100) - sum_of_square(100)
    print(res)
