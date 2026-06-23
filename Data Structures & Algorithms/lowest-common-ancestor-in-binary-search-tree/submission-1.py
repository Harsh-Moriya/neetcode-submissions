# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Function to find a path from a node to the target (one of the given nodes)
        def findPath(node, target, current_path):
            # Early return
            if not node:
                return False

            # Append assuming current node is on path
            current_path.append(node) 

            # If target is found then no need to continue
            if node.val == target.val:
                return True

            # Check for left and right subtrees recursively and build the path, if any returns true then current node is also on path so return true
            if findPath(node.left, target, current_path) or findPath(node.right, target, current_path):
                return True

            # If this is an invalid path then backtrack
            current_path.pop()

            return False

        path_to_p = []
        path_to_q = []

        findPath(root, p, path_to_p)
        findPath(root, q, path_to_q)

        # Run a loop using the smaller path and find the last common node/ancestor
        lca = None
        for i in range(min(len(path_to_p), len(path_to_q))):
            if path_to_p[i].val == path_to_q[i].val:
                lca = path_to_p[i]
            else:
                break

        return lca