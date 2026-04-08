class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        total_array = set()

        for i in nums:
            total_array.add(i)
        if len(total_array) != len(nums):
            return True 
        else:
            return False

            