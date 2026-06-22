# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If subRoot is null then it is definitely a subtree
        if not subRoot:
            return True
        # If subRoot is not null (since we reached here) and root is null then it is definitely not a subtree
        if not root:
            return False

        # Check for current node
        if self.isSame(root, subRoot):
            return True

        # Recursively check for every child
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def isSame(self, p, q) -> bool:
        if not p and not q:
            return True

        if (not p or not q) or (p.val != q.val):
            return False

        return (self.isSame(p.left, q.left) and self.isSame(p.right, q.right))