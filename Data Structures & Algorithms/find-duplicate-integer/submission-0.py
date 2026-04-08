class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        nums contains n + 1 integers. 
        each integer in nums is in the range [1, n] inclusive 
        brute force: using a hashmap or set() would be 0(n) space
        """

        seen = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                return nums[i]
            else:
                seen.add(nums[i])

