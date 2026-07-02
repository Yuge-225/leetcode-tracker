# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = list1
        h2 = list2
        
        dummyNode = ListNode()
        cur = dummyNode

        while h1 and h2:
            if h1.val <= h2.val:
                cur.next = h1
                h1 = h1.next
                
            else:
                cur.next = h2
                h2 = h2.next
            
            cur = cur.next

        if not h1:
            cur.next = h2
        if not h2:
            cur.next = h1

        return dummyNode.next
            





"""
 p1 = list1
        p2 = list2
        dummy = ListNode(0,None)
        curr = dummy

        while p1 and p2:
            if p1.val <= p2.val:
                curr.next = p1
                p1 = p1.next
            else:
                curr.next = p2
                p2 = p2.next
            curr = curr.next
        curr.next = p1 if p1 else p2

            
        return dummy.next
"""