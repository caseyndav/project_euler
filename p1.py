#!/usr/bin/env python

# Problem 1: Multiples of 3 and 5
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the
# multiples of 3 or 5 below 1000.

import time

def sum_of_multiples_brute(divisors, n):
    """
    Brute force solution: Check every integer from 0 to n, try dividing by each
    divisor. If modulus is zero, add to sum, and continue loop.
    """
    divisors = set(divisors)
    summation = 0
    for i in xrange(n):
        for div in divisors:
            if div == 0: continue
            if i % div == 0:
                summation += i
                break
    return summation

def sum_of_multiples_smarter(divisors, n):
    """
    This solution takes each divisor and multiplies it by consecutive integers
    and finds each product that is less than n, summing all of these products. A
    set is used here to ensure no products are added more than once to the sum.
    """
    divisors = set(divisors) # Remove any duplicates
    set_of_products = set()
    for div in divisors:
        if div == 0: continue
        i = 1
        product = 0
        while div * i < n:
            set_of_products.add(div * i)
            i += 1
    summation = sum(set_of_products)
    return summation

if __name__ == "__main__":
    n = 1000
    divisors = [3, 5]
    print sum_of_multiples_smarter(divisors, n)