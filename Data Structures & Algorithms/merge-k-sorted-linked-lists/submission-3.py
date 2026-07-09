# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class NodeWrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return other.node.val > self.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for l in lists:
            heapq.heappush(heap, NodeWrapper(l))

        head = ListNode()
        curr = head
        while heap:
            node = heapq.heappop(heap).node
            curr.next = ListNode(node.val)
            curr = curr.next
            if node.next:
                heapq.heappush(heap, NodeWrapper(node.next))
            
        return head.next