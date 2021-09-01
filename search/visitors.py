class DepthsVisitor:
    """ Visitor that returns a descriptive string of tree's nodes with value and depth """
    def visit(self, node, depth=0):
        if not node: return

        left  = self.visit(node.left,  depth+1)
        right = self.visit(node.right, depth+1)

        return f'({left}) {node.value}:{depth} ({right})'

class DeepestVisitorHelper:
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

class DeepestVisitor:
    """ Visitor that returns a string describing deepest nodes and depth """
    def visit(self, node):
        memo = DeepestVisitorHelper().visit(node)
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
