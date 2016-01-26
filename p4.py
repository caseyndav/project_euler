#!/usr/bin/env python

# Problem 4: Largest palindrome product
#
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 × 99. Find the largest
# palindrome made from the product of two 3-digit numbers.

def largest_palindrome_product(n):
    """
    Finds the largest palindrome product of two n-digit numbers by multiplying
    every possible pair of n-digit integers from largest to smallest. This
    ensures the largest palindrome product will always be the first one found.
    """
    begin = 10 ** (n - 1)
    end = 10 ** n
    for i in xrange(end - 1, begin - 1, -1): # Traverse loops backwards
        for j in xrange(end - 1, begin - 1, -1):
            product = i * j
            forward = str(product)
            reverse = forward[::-1]
            if (forward == reverse): # Check if palindrome
                return product
    return None

if __name__ == "__main__":
    n = 3
    print largest_palindrome_product(n)