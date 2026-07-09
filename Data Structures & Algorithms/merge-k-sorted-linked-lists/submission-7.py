# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class NodeWrapper:
    def __init__(self, node):
        self.next = node.next
        self.val = node.val

    def __lt__(self, other):
        return other.val > self.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        heap = []
        for lst in lists:
            if lst:
                heapq.heappush(heap, NodeWrapper(lst))

        dummy = ListNode()
        curr = dummy
        while heap:
            node = heapq.heappop(heap)
            curr.next = ListNode(node.val)
            curr = curr.next
            if node.next:
                heapq.heappush(heap, NodeWrapper(node.next))
        return dummy.next
