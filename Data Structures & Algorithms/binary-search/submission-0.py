class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        given a list of integers num 
        brute force, i should find the median of the list 
        if that index holds the target, return 
        if the target is less than the median, i put the r pointer there 
        then put the l pointer at the 

        """
        return self.binary_search(0, len(nums) - 1, nums, target)

    def binary_search(self, l: int, r: int, nums: list[int], target: int):
        if l > r:
            return -1 

        m = l + (r - l) // 2

        if nums[m] == target:
            return m
        elif nums[m] > target:
            return self.binary_search(l, m - 1, nums, target)
        else:
            return self.binary_search(m + 1, r, nums, target)
        





        
