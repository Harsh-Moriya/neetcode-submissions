# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Global max tracker, we use list here because we can't directly update a variable value in local scope in python so we update the value IN the list
        res = [float('-inf')]

        def dfs(node):
            # Base case
            if not node:
                return 0

            # Get max path sums for the left and right subtrees, if negative then we'll use zero (basically discarding the negative sums)
            left_max = max(0, dfs(node.left))
            right_max = max(0, dfs(node.right))

            # Update the max, consider that this node splits
            res[0] = max(res[0], node.val + left_max + right_max)

            # A split can only occur once which we are handling with the global var, as for the return, a parent dfs expects only the max path sum from the child dfs and assumes it won't split as the parent considers self to be the split.
            return node.val + max(left_max, right_max)

        dfs(root)

        return res[0]