# Number letter counts
# Problem 17

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

# Answer: 21124

num_dict = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
    15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
    20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety',
    100: 'hundred'
}


def num_to_words(num):
    '''
    convert numbers between 1 and 1000 to words
    '''
    hundreds = num // 100
    tens = (num - hundreds * 100) // 10
    ones = num % 10

    if hundreds == 10:
        return 'one thousand'

    words = []
    if hundreds > 0:
        words.append(num_dict[hundreds])
        words.append('hundred')
        if tens != 0 or ones != 0:
            words.append('and')

    if tens >= 2:
        word = []
        word.append(num_dict[tens * 10])
        if ones > 0:
            word.append(num_dict[ones])
        words.append('-'.join(word))
    elif tens == 1 or ones > 0:
        words.append(num_dict[10 * tens + ones])

    return ' '.join(words)


def main():
    length = 0
    for n in xrange(1000):
        word = num_to_words(n+1).replace(' ', '').replace('-', '')
        length += len(word)
    print length


if __name__ == '__main__':
    main()
