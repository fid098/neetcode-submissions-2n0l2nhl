class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        array size n 
        return elemnt that appears more than n/2 times 
        """

        hashmap = {}

        for i in range(len(nums)):
            if nums[i] in hashmap:
                hashmap[nums[i]] += 1
            else:
                hashmap[nums[i]] = 1
        
        majority = len(nums) //  2
        for key, value in hashmap.items():
            if value > majority:
                return key

        