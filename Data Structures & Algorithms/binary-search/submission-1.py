class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        given a list of integers num 
        i should find the median of the list 
        if that index holds the target, return 
        if the target is less than the median, i put the r pointer there 
        then put the l pointer at the 
        brute force: make it recursive and define anothe function that takes 
        the l, r, array, target to find the index

        [1,2,3,4,5,6]
        target 2     
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + ((r - l) // 2)

            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid 
        return -1 






        
