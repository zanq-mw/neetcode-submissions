# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def helper(l1, l2, carry):
            if not l1 and not l2 and not carry:
                return None
            
            first = l1.val if l1 else 0
            second = l2.val if l2 else 0

            firstnext = l1.next if l1 else None
            secondnext= l2.next if l2 else None

            total = (first + second + carry) % 10
            carry = (first + second + carry) // 10
            node = ListNode(total)
            node.next = helper(firstnext, secondnext, carry)
            return node
        
        return helper(l1, l2, 0)