# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        while list1 is not None or list2 is not None:
            if head.next:
                print(head.next.val)
            if list1 is None:
                curr.next = list2
                list2 = list2.next
            elif list2 is None:
                curr.next = list1
                list1 = list1.next
            elif list2.val < list1.val:
                curr.next = list2
                list2 = list2.next
            else:
                curr.next = list1
                list1 = list1.next
            curr = curr.next
        
        return head.next