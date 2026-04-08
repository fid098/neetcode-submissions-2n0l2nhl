# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        optimal:
        we want to traverse once to find the total nodes 
        find the index to remove
        if that index == 0, delete the head, return head.next
        traverse again until we reach the node before the index
        update the next pointer to skip the unwanted node 
        return the modified head
        """

        N = 0
        cur = head 
        while cur:
            N += 1
            cur = cur.next

        removeIndex = N - n
        if removeIndex == 0:
            return head.next

        cur = head
        for i in range(N - 1):
            if (i + 1) == removeIndex:
                cur.next = cur.next.next
                break
            cur = cur.next
        return head 
    
        

