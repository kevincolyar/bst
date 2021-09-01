import logging

logger = logging.getLogger(__name__)

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

    def visit(self, visitor, *args, **kwargs):
        """ Visit nodes of the BST, beginning with the root """
        return visitor.visit(self.root, *args, **kwargs)

    def search(self, key):
        """ Searches BST with given key, returning None if not found. """
        return SearchVisitor().visit(self.root, key)

class Node:
    def __init__(self):
        self.key   = None
        self.value = None
        self.left  = None
        self.right = None

    def insert(self, key, value=None):
        if self.key == None:
            self.key = key
            self.value = value or key

        # Key is less than current, insert left
        elif key < self.key:
            self.left = self.left or Node()
            self.left.insert(key, value)

        # Key is greater than current, insert right
        elif key > self.key:
            self.right = self.right or Node()
            self.right.insert(key, value)

        return self

class StdOutVisitor:
    def visit(self, node):
        if not node: return

        left  = self.visit(node.left)
        right = self.visit(node.right)

        return f'({left}) {node.value} ({right})'

class DepthVisitor:
    def visit(self, node, depth=0):
        if not node: return

        left  = self.visit(node.left,  depth+1)
        right = self.visit(node.right, depth+1)

        return f'({left}) {node.value};{depth} ({right})'

class DeepestVisitor:
    def visit(self, node, depth=0, memo={}):
        if not node: return memo

        left  = self.visit(node.left,  depth+1, memo)
        right = self.visit(node.right, depth+1, memo)

        if depth not in memo: memo[depth] = []

        memo[depth].append(node.value)

        return memo

class DeepestOutputVisitor:
    def visit(self, node):
        memo = DeepestVisitor().visit(node)
        depth = sorted(memo.keys())[-1]
        deepest = ', '.join({str(i) for i in memo[depth]})

        return f'deepest, {deepest}; depth, {depth}'

class SearchVisitor:
    def visit(self, node, key):
        if not node: return None

        if node.key == key:
            return node.value

        if key < node.key:
            return self.visit(node.left, key)
        elif key > node.key:
            return self.visit(node.right, key)
