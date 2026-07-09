# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return
        slow = head
        fast = head.next
        count = 0
        while fast and fast.next:
            count+=1
            slow=slow.next
            fast = fast.next.next

        reverse = None
        second = slow.next
        slow.next = None
        while second:
            tmp = second.next
            second.next = reverse
            reverse = second
            second = tmp
        curr = head
        while reverse:
            tmp = curr.next
            tmp2 = reverse.next
            curr.next = reverse
            reverse.next = tmp
            curr = tmp
            reverse = tmp2
        

        
