class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res, sol = [], []

        def backtrack(i):
            res.append(sol[:])

            for j in range(i, len(nums)):
                #check if its a duplicate
                if j > i and (nums[j] == nums[j - 1]):
                    continue 

                #if we pick the value 
                sol.append(nums[j])
                backtrack(j + 1)

                #if we dont pick the value
                sol.pop()
        
        backtrack(0)
        return res 
                