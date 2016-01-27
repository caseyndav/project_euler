#!/usr/bin/env python

# Problem 3: Largest prime factor
#
# The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime
# factor of the number 600851475143?

import tree
import factor


def largest_prime_factor(n):
    """
    Generates a factor tree then performs depth-first search to find largest
    prime factor.
    """
    t = tree.Tree(n)
    factor.factor(t)
    largest = dfs(t)
    return largest


def dfs(t):
    """
    Basic depth-first search algorithm to find the largest prime factor (leaf)
    in the tree.
    """
    if (not t.has_children()):
        return t.data
    largest1 = dfs(t.child1)
    largest2 = dfs(t.child2)
    if (largest1 > largest2):
        return largest1
    return largest2

if __name__ == "__main__":
    n = 600851475143
    print largest_prime_factor(n)
