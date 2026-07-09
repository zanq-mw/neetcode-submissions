# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def buildList(node):
            if not node:
                return []
            lft = buildList(node.left)
            right = buildList(node.right)
            return lft + [node.val] + right
        
        return buildList(root)[k-1]
            