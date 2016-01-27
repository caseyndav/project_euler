#!/usr/bin/env python

import sys


class Tree(object):
    """
    Basic tree data structure.
    """

    def __init__(self, data):
        self.child1 = None
        self.child2 = None
        self.data = data

    def has_children(self):
        if (self.child1 is not None or self.child2 is not None):
            return True
        return False

    def get_leaves(self):
        leaves = []
        if (not self.has_children()):
            leaves.append(self.data)
            return leaves
        leaves += self.child1.get_leaves()
        leaves += self.child2.get_leaves()
        return leaves

    def print_tree(self, root=True):
        sys.stdout.write(str(self.data))
        if (self.has_children()):
            sys.stdout.write(" {")
            self.child1.print_tree(False)
            sys.stdout.write(", ")
            self.child2.print_tree(False)
            sys.stdout.write("}")
        if (root):
            sys.stdout.write("\n")
