class BSTnode(object):
    """
Representation of a node in a binary search tree.
Has a left child, right child, and key value, and stores its subtree size.
"""
    def __init__(self, parent, t):
        """Create a new leaf with key t."""
        self.key = t
        self.parent = parent
        self.left = None
        self.right = None
        self.size = 1
        
    def update_stats(self):
        """Updates this node's size based on its children's sizes."""
        self.size = (0 if self.left is None else self.left.size) + (0 if self.right is None else self.right.size) 

    def insert(self, t, NodeType):
        """Insert key t into the subtree rooted at this node (updating subtree size)."""
        self.size += 1
        if t < self.key:
            if self.left is None:
                self.left = NodeType(self, t)                
                return self.left
            else:
                return self.left.insert(t, NodeType)
        else:
            if self.right is None:
                self.right = NodeType(self, t)   
                return self.right
            else:
                return self.right.insert(t, NodeType)
