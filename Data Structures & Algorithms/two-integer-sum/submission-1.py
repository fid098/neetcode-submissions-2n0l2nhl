class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, value in enumerate(nums):
            #loop through the list getting the value and in the index
            n = target - value
            #get the difference
            if n in hashmap:
                #if the difference is in the hashmap
                return [hashmap[n], i]
                #return the index of the difference and the current index
            hashmap[value] = i
            #or add the current value and index to the hashmap 
        return

        