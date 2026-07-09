# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        q = deque()
        q.append(root)
        res = ""

        while q:
            node = q.popleft()
            if node:
                res += str(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                res += '/'
            res += ","
        
        return res
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "/,":
            return None
        data=data.split(",")[0:-1]
        for i in range(len(data)):
            if data[i] == "/":
                data[i] = None
            else:
                data[i] = int(data[i])

        root = TreeNode(data[0])
        q = deque()
        q.append(root)
        i = 1
        while q and i<len(data):
            node = q.popleft()
            if data[i] is not None:
                node.left = TreeNode(data[i])
                q.append(node.left)
            i+=1
            if i<len(data) and data[i] is not None:
                node.right = TreeNode(data[i])
                q.append(node.right)
            i+=1
        return root

