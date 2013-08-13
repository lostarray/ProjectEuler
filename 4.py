# Largest palindrome product
# Problem 4

# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# Answer: 906609


def is_palindrome(num):
    if int(str(num)[::-1]) == num:
        return True
    return False


def max_palindrome(digits):
    palindrome = 0
    x = 10**digits - 1
    while x >= 10**(digits-1) - 1:
        y = 10**digits - 1
        while y >= x:
            product = x * y
            if is_palindrome(product) and product > palindrome:
                palindrome = product
            elif product < palindrome:
                break
            y -= 1
        x -= 1
    return palindrome


if __name__ == '__main__':
    print(max_palindrome(3))
