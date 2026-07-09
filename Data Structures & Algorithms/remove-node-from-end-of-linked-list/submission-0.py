# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 0
        while curr:
            count+=1
            curr = curr.next
        curr = head
        i= 0
        target = count - n
        if target == 0:
            return head.next
            
        while i+1<target:
            curr=curr.next
            i+=1
        
        curr.next = curr.next.next
        return head