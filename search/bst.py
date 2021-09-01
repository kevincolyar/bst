from search.node import Node
from search.visitors import SearchVisitor, DepthsVisitor, DeepestVisitor

class Bst:
    def __init__(self, *args):
        """ Create initial binary search tree of comparable items"""
        self.root = Node()

        self.insert(*args)

    def insert(self, *args):
        """ Insert collection of comparable items """
        for i in args:
              self.root.insert(i)

        return self

    def search(self, key):
        """ Searches BST with given key, returning None if not found. """
        return SearchVisitor().visit(self.root, key)

    def depths(self):
        """ Outputs tree's nodes with value and depth """
        return DepthsVisitor().visit(self.root)

    def deepest(self):
        """ Outputs the deepest nodes in the BST, along with the depth"""
        return DeepestVisitor().visit(self.root)
