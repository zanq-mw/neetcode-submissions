# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedlists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = None
                if len(lists) > i+1:
                    l2 = lists[i+1]
                mergedlists.append(self.mergeLists(l1, l2))
            lists = mergedlists
        return lists[0]
        # sortedlst = ListNode()

        # for lst in lists:
        #     curr = lst
        #     sortedcurr = sortedlst
        #     while sortedcurr.next and curr:
        #         if sortedcurr.next.val >= curr.val:
        #             tmp, tmp2 = sortedcurr.next, curr.next
        #             sortedcurr.next = curr
        #             curr.next = tmp
        #             curr = tmp2
        #         sortedcurr = sortedcurr.next

        #     if not sortedcurr.next:
        #         sortedcurr.next = curr
        # return sortedlst.next

    def mergeLists(self, lst1, lst2):
        head = ListNode()
        curr = head
        while lst1 and lst2:
            if lst1.val < lst2.val:
                curr.next = lst1
                lst1 = lst1.next
            else:
                curr.next = lst2
                lst2 = lst2.next
            curr = curr.next
        if lst1:
            curr.next = lst1
        elif lst2:
            curr.next = lst2
        return head.next