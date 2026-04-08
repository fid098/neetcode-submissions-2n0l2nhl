class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1  #start prefix as 1
        for i in range(len(nums)): # as we iterate through from the start
            res[i] = prefix   #first index is prefix 
            prefix *= nums[i]  #prefix is = prefix * current index
        postfix = 1 
        for i in range(len(nums) -1, -1, -1): #we iterate from the end 
            res[i] = res[i] * postfix  #res[i] already holds the prefix, so we mul that with postfix
            postfix *= nums[i] #postfix = postfix * current index
        return res 