# Power digit sum
# Problem 16

# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

# Answer: 1366

num = 2 ** 1000
digits = map(int, str(num))
print(sum(digits))
