# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists) > 1:
            tmp = []
            for i in range(0, len(lists), 2):
                if i == len(lists)-1:
                    tmp.append(lists[i])
                    continue
                first, second = lists[i], lists[i+1]
                output = ListNode()
                curr = output
                while first and second:
                    if first.val > second.val:
                        curr.next = second
                        second = second.next
                    else:
                        curr.next = first
                        first = first.next
                    curr = curr.next
                if first:
                    curr.next = first
                if second:
                    curr.next = second
                tmp.append(output.next)
            lists = tmp

        return lists[0]