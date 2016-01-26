#!/usr/bin/env python

# Problem 5: Smallest multiple
#
# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder. What is the smallest positive number that is
# evenly divisible by all of the numbers from 1 to 20?

import factor as f
import tree
from collections import defaultdict

def smallest_multiple(divisors):
	"""
	Returns the smallest positive integer evenly divisible by all of the
	integers in divisors.
	"""

	# Maps each prime factor to a count (e.g. 8 factors into three 2s, so its
	# map would look like {2 : 3}).
	factor_counts = defaultdict(int)

	# Factor all integers in the list of divisors.
	for d in divisors:
		t = tree.Tree(d)
		f.factor(t)

		# Count up the num of occurrences of each prime factor.
		leaf_counts = defaultdict(int) # defaultdict sets initial counts to 0
		for leaf in t.get_leaves():
			leaf_counts[leaf] += 1

		# If num of occurrences of a factor exceeds what we already have, change
		# count to the larger value (e.g. a number needs at least three 2s in
		# its list of prime factors in order to be divisible by 8).
		for leaf in leaf_counts:
			if (factor_counts[leaf] < leaf_counts[leaf]):
				factor_counts[leaf] = leaf_counts[leaf]

	# Now that we have a count of all prime factors for our smallest multiple,
	# we multiply them all together.
	smallest_multiple = 1
	for factor in factor_counts:
		smallest_multiple *= factor ** factor_counts[factor]
	return smallest_multiple

if __name__ == "__main__":
	divisors = range(1, 21) # Integers 1..20
	print smallest_multiple(divisors)