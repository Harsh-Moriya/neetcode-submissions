# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Base case
        if not root:
            return []

        # Queue to traverse the nodes
        q = deque([root])
        res = []

        while q:
            # At this poinst all nodes for a level must be in the queue
            level_size = len(q)
            level_vals = []

            # Loop to resolve all nodes of a level and push all nodes of the next level to queue
            for _ in range(level_size):
                # Take one node per iteration
                node = q.popleft()
                level_vals.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level_vals)

        return res