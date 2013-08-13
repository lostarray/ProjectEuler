# Largest prime factor
# Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

# Answer:6857


def max_prime_factor(num):
    n, i = num, 2
    while i <= n/2:
        if n % i == 0:
            n /= i
        else:
            i += 1
    if n == num:
        return None
    return max(i, n)

if __name__ == '__main__':
    print(max_prime_factor(600851475143))
