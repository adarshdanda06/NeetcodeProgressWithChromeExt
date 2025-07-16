# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if (head.next == None or head.next.next == None):
            return
    
        copy = ListNode(0, head)
        curr = head
        while (curr and curr.next):
            r = curr
            prev = ListNode(0, r)
            while (r.next != None):
                r = r.next
                prev = prev.next
            l = curr.next
            prev.next = None
            curr.next = r
            r.next = l
            l = l.next
            curr = l
            r = curr
        