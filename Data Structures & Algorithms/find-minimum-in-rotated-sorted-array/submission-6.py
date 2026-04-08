class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        given an array of length n, originally sorted in ascending order
        now rotated between 1 and n times 
        rotating means shifting it right by 1 - n times 
        assume all elements in the sorted array are unique
        brute force: use the min() function 
        put l at first index, and r and far right 
        if l > r then it has been rotated, find the mid
        if mid > r, min is in right side
        if mid < r, min is in left side
        return the l index 
        """
        l, r = 0, len(nums) - 1

        while l < r:
            if nums[l] <= nums[r]:
                return nums[l]

            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        return nums[l]

            