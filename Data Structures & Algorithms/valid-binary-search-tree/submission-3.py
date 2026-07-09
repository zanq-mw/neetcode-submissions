# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node, minBoundary, maxBoundary):
            if not node:
                return True
            if node.val > minBoundary and node.val < maxBoundary:
                return isValid(node.right, node.val, maxBoundary) and isValid(node.left, minBoundary, node.val)
            return False
        
        return isValid(root, -1001, 1001)