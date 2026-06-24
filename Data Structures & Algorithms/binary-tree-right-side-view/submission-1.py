# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, depth):
            if not node:
                return

            # Check if this is the first time this depth is reached, if its the first then res will have one items per previous level so it will match the depth if it's the first time, i.e. as long as depth started at 0
            if depth == len(res):
                res.append(node.val)

            # Traverse Right side first, this way we can ensure that only the rightmost node will be resolved first for any depth 
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

            return
            
        dfs(root, 0)

        return res