#!/usr/bin/env python

import tree

def factor(t):
	"""
	Factors using tree t as root node by checking if number is divisible by any
	number from 2 to (n/2 + 1).
	"""
	for i in xrange(2, t.data / 2 + 1):
		if (t.data % i == 0):
			t.child1 = tree.Tree(i)
			t.child2 = tree.Tree(t.data / i)
			factor(t.child1)
			factor(t.child2)
			break