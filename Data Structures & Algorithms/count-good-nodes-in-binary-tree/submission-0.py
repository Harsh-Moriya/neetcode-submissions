# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxVal):
            # Base case
            if not node:
                return 0

            # Current node counts as a good node if it's value is greater than or equal to the running max
            res = 1 if node.val >= maxVal else 0

            # Update the running max
            maxVal = max(maxVal, node.val)

            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)

            return res

        # Root is always a good node as it is the first and last on its path
        return dfs(root, root.val)