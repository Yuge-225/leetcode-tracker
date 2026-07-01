# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        cycleFound = False

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                cycleFound = True
                break
            
        if cycleFound:
            fast = head
            while fast != slow:
                fast = fast.next
                slow = slow.next
            return slow
        else:
            return None
        
        



"""
fast = slow = head
        cycleFound = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            # fill in the blank
            if fast == slow:
                cycleFound = True
                break

        if cycleFound:
            fast = head
            while fast != slow:
                fast = fast.next
                slow = slow.next
            return slow
                
        return None
"""