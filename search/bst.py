import logging

logger = logging.getLogger(__name__)

class Bst:
    def __init__(self, *args):
        self.root = Node()

        for i in args:
            self.root.insert(i)

    def visit(self, visitor):
        return visitor.visit(self.root)

class Node:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

    def insert(self, value):
        if self.value == None:
            self.value = value
        elif value < self.value:
            self.left = self.left or Node()
            self.left.insert(value)
        elif value > self.value:
            self.right = self.right or Node()
            self.right.insert(value)

        return self

class StdOutVisitor:
    def visit(self, node):
        left  = node.left and self.visit(node.left)
        right = node.right and self.visit(node.right)

        return f'({left}) {node.value} ({right})'

class DepthVisitor:
    def visit(self, node, depth=0):
        left  = node.left  and self.visit(node.left,  depth+1)
        right = node.right and self.visit(node.right, depth+1)

        return f'({left}) {node.value};{depth} ({right})'

class DeepestVisitor:
    def visit(self, node, depth=0, memo={}):
        left  = node.left  and self.visit(node.left,  depth+1, memo)
        right = node.right and self.visit(node.right, depth+1, memo)

        if depth not in memo:
            memo[depth] = []

        memo[depth].append(node.value)

        return memo

class DeepestOutputVisitor:
    def visit(self, node):
        memo = DeepestVisitor().visit(node)
        depth = sorted(memo.keys())[-1]
        deepest = ', '.join({str(i) for i in memo[depth]})

        return f'deepest, {deepest}; depth, {depth}'
