# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        we want to iterate throught he linked list
        we can use two pointers, slow and a fast 
        the slow iterates one at a time 
        the fast iterates two at a time
        if at any fast = slow, then we return true
        """

        slow = head 
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True 

        return False
        

