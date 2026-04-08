# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        we could split the list into two 
        reverse the second half 
        interweave both lists 
        """

        #find the middle
        slow = head
        fast = head 

        #for even and odd lists
        while fast.next and fast.next.next:
            slow = slow.next 
            fast = fast.next.next
        
        #second starts where slow is
        second = slow.next 
        slow.next = None 


        #reverse the second list
        prev = 0
        while second:
            nxt = second.next
            second.next = prev 
            prev = second 
            second = nxt 
        second = prev

        #interweave both lists 
        first = head 
        while second:
            #store the next nodes of both 
            temp1 = first.next
            temp2 = second.next 

            #interweave both 
            first.next = second 
            second.next = temp1

            #move both forward 
            first = temp1
            second = temp2





            
            


        
        