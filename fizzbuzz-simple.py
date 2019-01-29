#!/usr/bin/env python3

if __name__ == '__main__':
    # remember the rules:
    # - if the number is divisible by 3, print 'fizz'
    # - if the number is divisible by 5, print 'buzz'
    # - if the number is divisible by 3 AND 5, print 'fizzbuzz'
    # - otherwise, print the number

    # note the 101 in the `range()` call -- it's a count
    # of the numbers to be generated, not the last number
    # to use. in our case, we're starting at 0, so we're
    # generating 101 numbers, not 100.
    for number in range(0,101):
        # here we could use:
        # if (0 == number % 5) and (0 == number % 3):
        # but since we know that 15 is the common denominator
        # between 3 and 5, we can just use 15 instead and
        # save the interpreter a few instructions
        if (0 == number % 15):
            # this needs to be the first condition. if not,
            # either of the other conditions will fire first, and
            # short-cut the 'fizzbuzz' condition out.
            print('fizzbuzz')
        elif (0 == number % 5):
            # between 5 and 3 the order doesn't really matter,
            # so we're choosing a decreasing divisor because
            # it looks nice
            print('buzz')
        elif (0 == number % 3):
            print('fizz')
        else:
            # if all else fails, just print the number
            print(number)
