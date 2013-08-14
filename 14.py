# Longest Collatz sequence
# Problem 14

# The following iterative sequence is defined for the set of positive integers:
#     n -> n/2 (n is even)
#     n -> 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
#         13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

# Answer: 837799


def trans(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1


def len_of_chains(limit):
    chain_length = [0 for n in range(limit + 1)]
    chain_length[1] = 1
    for i in range(1, limit + 1):
        if chain_length[i] > 0:
            continue
        chain = [i]
        n = i
        while n != 1:
            n = trans(n)
            chain.insert(0, n)
            if n <= limit and chain_length[n] > 0:
                break
        for t in range(1, len(chain)):
            if chain[t] <= limit:
                chain_length[chain[t]] = chain_length[chain[0]] + t
    return chain_length


if __name__ == '__main__':
    chain_length = len_of_chains(1000000)
    print(chain_length.index(max(chain_length)))
