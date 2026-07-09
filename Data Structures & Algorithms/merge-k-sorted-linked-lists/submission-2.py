# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        holder = []
        for lst in lists:
            while lst is not None:
                heapq.heappush(holder, lst.val)
                lst = lst.next
        
        head = ListNode()
        curr = head
        while holder:
            curr.next = ListNode(heapq.heappop(holder))
            curr = curr.next
        return head.next