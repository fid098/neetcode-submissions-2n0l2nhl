# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        initialise a dummy node which would start from null
        we compare the values of each list and attach it to the dummy node 
        at the end of the comparison, if one list is bigger than the other,
        we can just add that list to the end of the dummy list 
        return the dummy head which would be dummy.next
        """

        dummy = ListNode(0) #null
        current = dummy 

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return dummy.next

        