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
