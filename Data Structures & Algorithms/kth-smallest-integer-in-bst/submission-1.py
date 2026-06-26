# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        node_vals = []

        def dfs(node):
            if not node:
                return

            dfs(node.left)

            node_vals.append(node.val)
            
            dfs(node.right)

            return

        dfs(root)

        node_vals.sort()

        return node_vals[k - 1]