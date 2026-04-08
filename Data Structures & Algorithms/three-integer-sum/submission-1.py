class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        triplets that add up to zero, and the indices i,j,k are all distinct
        we could use a hashlist
        we check each group of three if they add up to 0
        l pointer at start, right next to it
        the output should not contain any duplicate triplets
        """

        res = []
        nums.sort()

        for i, a in enumerate(nums): #we get the index i and the value a
            if a > 0:
                break 

            if i > 0 and a == nums[i - 1]:  #if not the first item and value at that index is the same as value at previous index, skip 
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1 
                elif threesum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:  #while the are duplcates and l < r, increment l 
                        l += 1
        return res

