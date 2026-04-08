class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """

        prefix = [1, 1, 2, 0]
        nums = [1,2,0,6]
        postfix = [0, 0, 6, 1]

        output = [48, 24, 12, 8] 

        res = [1,1,1,1]
        """

        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) -1, -1, -1):
            res[i] = res[i] * postfix
            postfix *= nums[i]
        
        return res

