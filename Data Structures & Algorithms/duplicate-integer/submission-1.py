class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        total_array = set()
        for i in nums:
            if i in total_array:
                return True
            total_array.add(i)
        return False
            