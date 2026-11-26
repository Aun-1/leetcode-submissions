# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def maxDepth(root):
            nonlocal best
            if root is None:
                return 0
            left=maxDepth(root.left)
            right=maxDepth(root.right)
            best = max(best, left + right)
            return 1 + max(left, right)
        

        best = 0
        maxDepth(root)
        return best