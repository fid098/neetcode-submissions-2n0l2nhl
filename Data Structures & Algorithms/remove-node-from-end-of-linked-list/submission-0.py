# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        brute force:
        load the list into an array
        remove the index from the end 
        and rebuild the linked list 
        """

        #load into array
        nodes = []
        current = head
        while current != None:
            nodes.append(current.val)
            current = current.next

        #remove the index
        del nodes[-n]
        result = nodes 
        

        #rebuild the linked list with results array
        dummy = ListNode(0)
        current = dummy
        for i in result:
            current.next = ListNode(i)
            current = current.next

        return dummy.next 


