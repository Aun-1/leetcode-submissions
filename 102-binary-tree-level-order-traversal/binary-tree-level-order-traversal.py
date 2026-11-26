# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
        result = []
        queue = deque([root])
        while queue:
            level = []                          # this ring's values
            for _ in range(len(queue)):         # exactly one level
                node = queue.popleft()
                level.append(node.val)          # ← CHANGES: what you record per level
                if node.left:
                    queue.append(node.left)     # the children go into the next level
                if node.right:
                    queue.append(node.right)
            result.append(level)                # ← CHANGES: what you save per level
        return result