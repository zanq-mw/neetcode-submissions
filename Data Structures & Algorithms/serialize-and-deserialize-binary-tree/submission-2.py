# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        q = deque()
        q.append(root)
        lst = []

        while q:
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if node:
                    lst.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    lst.append(None)

        s = ""
        for c in lst:
            if c:
                s += str(c) + "n"
            else:
                s += "/n"
        return s

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        lst = data.split("n")
        for i in range(len(lst)):
            if lst[i] == "/":
                lst[i] = None
        # lst = []
        # for c in data:
        #     if c == "/":
        #         lst.append(None)
        #     else:
        #         lst.append(int(c))

        # if not lst:
        #     return None
        
        i = 1
        root = TreeNode(lst[0])
        q = deque()
        q.append(root)
        while q and i < len(lst):
            node = q.popleft()
            if lst[i] is not None:
                node.left = TreeNode(lst[i])
                q.append(node.left)
            i += 1
            
            if i< len(lst) and lst[i] is not None:
                node.right = TreeNode(lst[i])
                q.append(node.right)
            i+=1
        return root


        

