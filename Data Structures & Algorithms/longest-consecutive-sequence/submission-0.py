class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        we are given list of integers 
        and need to find a list of consequtive numbers 
        consequtive: number before is 1 less than current 
        brute force: sort the list and iterate throught the array

        [0,1,1,2,3,4,5,6]
        """

        numSet = set(nums)
        max_value = 0 

        for n in nums:
            if (n - 1) not in numSet:  #while the previous num is not in the set 
                length = 1  #this num is the start of the sequence
                while (n + length) in numSet:   #while the num + length of the sequence is in the numset
                    length += 1  #increment the length
        
                max_value = max(max_value, length)  #the max sequence is the max 
        return max_value