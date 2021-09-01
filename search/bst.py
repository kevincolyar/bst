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

    def deepest(self):
        """ Outputs the deepest nodes in the BST, along with the depth"""
        return DeepestOutputVisitor().visit(self.root)

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

class DepthVisitor:
    """ Visitor that returns a descriptive string of tree """
    def visit(self, node, depth=0):
        if not node: return

        left  = self.visit(node.left,  depth+1)
        right = self.visit(node.right, depth+1)

        return f'({left}) {node.value}:{depth} ({right})'

class DeepestVisitor:
    """ Visitor that returns a dict of values grouped by depth """
    def visit(self, node, depth=0, memo=None):
        # TODO: Ideally this would be a default argument, but python caches mutable default arguments (?)
        if memo is None:
            memo = {}

        if not node:
            return memo

        left  = self.visit(node.left,  depth+1, memo)
        right = self.visit(node.right, depth+1, memo)

        # Initialize depth collection if needed
        if depth not in memo:
            memo[depth] = []

        # Group node values by depth
        memo[depth].append(node.value)

        return memo

class DeepestOutputVisitor:
    """ Visitor that returns a string describing deepest nodes and depth """
    def visit(self, node):
        memo = DeepestVisitor().visit(node)
        depth = max(memo.keys())
        deepest = ','.join(str(i) for i in memo[depth])

        return f'deepest, {deepest}; depth, {depth}'

class SearchVisitor:
    """ Visitor that searches the tree for the given key, returning the node's value, or None if not found """
    def visit(self, node, key):
        if not node: return None

        if node.key == key:
            return node.value

        if key < node.key:
            return self.visit(node.left, key)
        elif key > node.key:
            return self.visit(node.right, key)
