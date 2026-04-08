# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        null -> 0 -> 1 -> 2 -> 3 -> null
        prev = null, current = head = 0
        while current != null, nxt = current.next, prev = current, current = nxt
        at the end, curr = null, prev = last value
        """

        prev, curr = None, head

        while curr:
            nxt = curr.next   #store the next value
            curr.next = prev  #reverse the pointer
            prev = curr    #move prev to curr
            curr = nxt     #move curr to next

        return prev