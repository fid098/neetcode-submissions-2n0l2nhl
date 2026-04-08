# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Convert to arrays
        list1, list2 = [], []
        
        curr1, curr2 = l1, l2
        while curr1:  # ✅ Process all of l1
            list1.append(curr1.val)
            curr1 = curr1.next
        
        while curr2:  # ✅ Process all of l2
            list2.append(curr2.val)
            curr2 = curr2.next
        
        # Step 2: Pad shorter list with zeros
        while len(list1) < len(list2):
            list1.append(0)
        while len(list2) < len(list1):
            list2.append(0)
        
        # Step 3: Add with carry
        res = []
        carry = 0
        
        for i in range(len(list1)):  # ✅ Start from 0
            total = list1[i] + list2[i] + carry
            res.append(total % 10)  # ✅ Store digit
            carry = total // 10     # ✅ Handle carry
        
        if carry:  # ✅ Don't forget final carry
            res.append(carry)
        
        # Step 4: Build linked list
        dummy = ListNode(0)
        current = dummy
        
        for val in res:
            current.next = ListNode(val)
            current = current.next
        
        return dummy.next
            
            





