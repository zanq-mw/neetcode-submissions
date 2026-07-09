# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sortedlst = ListNode()

        for lst in lists:
            curr = lst
            sortedcurr = sortedlst
            while sortedcurr.next and curr:
                if sortedcurr.next.val >= curr.val:
                    tmp, tmp2 = sortedcurr.next, curr.next
                    sortedcurr.next = curr
                    curr.next = tmp
                    curr = tmp2
                sortedcurr = sortedcurr.next

            if not sortedcurr.next:
                sortedcurr.next = curr
        return sortedlst.next