class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        brute force: use hashmap or set 
        optimal:
        we look at it as a linked list with the index pointing to the value 
        initialise slow and fast pointers 
        move slow once and fast two steps at a time 
        if there is a cycle, they will eventually meet 
        once they meet, start a new pointer from the beginning 
        move both one step at a time 
        when they meet again is the duplicate number
        """

        slow, fast = 0, 0 
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]  #place the fast at the value at the index of the value of the index of 0

            if slow == fast:
                break #they meet in the cycle 

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
        

