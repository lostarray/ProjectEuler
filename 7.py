# 10001st prime
# Problem 7

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

# Answer: 104743


def prime_num(index):
    prime = []
    num = 2
    while len(prime) < index:
        is_prime = True
        for n in prime:
            if n * n > num:
                break
            elif num % n == 0:
                is_prime = False
                break
        if is_prime:
            prime.append(num)
        num += 1
    return prime[-1]

if __name__ == '__main__':
    print(prime_num(10001))
