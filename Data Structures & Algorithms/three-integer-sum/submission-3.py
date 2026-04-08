class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        num.sort()
        iterate once to each index and the value using enumerate
        a, l = i + 1, r = len(num) - 1
        a + nums[l] + nums[r] == 0: we add it to the list
        > 0 : r -= 1
        < = : l += 1
        num[i] == num[i - 1], l += 1  
        """

        res = set()
        nums.sort()


        for i, a in enumerate(nums):
            r = len(nums) - 1
            l = i + 1
            while l < r:
                added_value = a + nums[l] + nums[r]
                if added_value == 0:
                    if tuple([a, nums[l], nums[r]]) not in res:
                        res.add(tuple([a, nums[l], nums[r]]))
                    l += 1
                    while (l < r) and (nums[l] == nums[l - 1]):
                        l += 1 
                elif added_value > 0:
                    r -= 1
                    while (l < r) and (nums[r] == nums[r + 1]):
                        r -= 1
                elif added_value < 0:
                    l += 1
                    while (l < r) and (nums[l] == nums[l - 1]):
                        l += 1
        return [list(i) for i in res] 
                    
                




        


