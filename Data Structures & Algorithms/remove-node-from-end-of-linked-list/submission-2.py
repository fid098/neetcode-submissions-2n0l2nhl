# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        optimal:
        use two pointers
        create a dummy node pointing to the head
        l = dummy
        right = head 
        move right forward n steps
        move both pointers until right = null
        now left.next is the node to delete 
        return dummy.next as the update head 
        """

        dummy = ListNode(0, head)
        left = dummy
        right = head

        #move the right by n steps 
        while n > 0:
            right = right.next
            n -= 1
        
        #move both 
        while right:
            left = left.next
            right = right.next

        #when the loop stops and right is at null
        #let left skip over the removed index
        left.next = left.next.next

        #return the new updated list 
        return dummy.next


