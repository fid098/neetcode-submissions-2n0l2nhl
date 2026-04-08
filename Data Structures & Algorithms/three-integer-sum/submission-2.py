class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        sort the array 
        iterate the array 1 to find the first number 
        set() to remove duplicates 
        """

        res = set()
        nums.sort()
        temp = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = [nums[i], nums[j], nums[k]]
                        res.add(tuple(temp))
        
        return [list(i) for i in res]
        


