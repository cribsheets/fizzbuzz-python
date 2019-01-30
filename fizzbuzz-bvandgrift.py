#!/usr/bin/env python3

# this solution is provided as an example of something
# that works, but is arguably too clever. this uses
# python's inline if/else structure to create a series
# of nested if/else clauses, returning the number as the
# last option.

# what makes this too clever? the else dangling into
# space might be harder to understand on a first reading,
# and doesn't appear to be well-formed python (even though
# it is).

# author: @bvandgrift

if __name__ == '__main__':

    for number in range(0, 101):
        print('fizzbuzz' if 0 == number % 15 else
              'buzz'     if 0 == number % 5  else
              'fizz'     if 0 == number % 3  else
              number)
