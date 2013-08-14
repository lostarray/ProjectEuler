# Lattice paths
# Problem 15

# Starting in the top left corner of a 2 x 2 grid, and only being able to move to the right and down,
# there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20 x 20 grid?

# Answer: 137846528820

from math import factorial


def c(m, n):
    return factorial(m) / (factorial(n) * factorial(m - n))

if __name__ == '__main__':
    print(c(40, 20))
