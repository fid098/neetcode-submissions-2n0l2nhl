class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        it is sorted in non-decreasing order 
        we are given a target 
        find the index of the two numbers that add up to this target 
        """
        l, r = 0, len(numbers) - 1 

        while l < r:
            cursum = numbers[l] + numbers[r]
            if cursum > target:
                r -= 1
            elif cursum < target:
                l += 1
            else:
                return [l + 1, r + 1]