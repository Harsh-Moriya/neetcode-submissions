# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Tracker for the ancestor
        current = root

        # Run a loop utilizing the unique property of the BST
        while current:
            # If the targets are less than the current then the ancestor is on the left side of the tree
            if p.val < current.val and q.val < current.val:
                current = current.left
            # If the targets are greater than the current then the ancestor is on the right side of the tree
            elif p.val > current.val and q.val > current.val:
                current = current.right
            # If one is greater and the other is smaller then the tree is about to split and our targets are in opposite sides of this split making our current node the common ancestor, one other case is that if atleast one of the targets is same as current in which case still the logic holds
            else:
                return current