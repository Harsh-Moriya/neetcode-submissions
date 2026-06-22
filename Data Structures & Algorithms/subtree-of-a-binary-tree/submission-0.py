# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = deque([root])

        while queue:
            node = queue.popleft()

            if not node:
                continue

            if node.val == subRoot.val and self.isSame(node, subRoot):
                return True
            
            queue.append(node.left)
            queue.append(node.right)

        return False

    def isSame(self, p, q) -> bool:
            queue = deque([(p, q)])

            while queue:
                node_p, node_q = queue.popleft()

                if not node_p and not node_q:
                    continue

                if (not node_p or not node_q) or (node_p.val != node_q.val):
                    return False

                queue.append((node_p.left, node_q.left))
                queue.append((node_p.right, node_q.right))

            return True