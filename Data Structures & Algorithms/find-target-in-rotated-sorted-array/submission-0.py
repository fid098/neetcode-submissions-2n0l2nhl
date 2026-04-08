class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        array of lenght n, originally sorted in ascending order 
        and rotated between 1 and n
        given the array nums and target, return index of target within nums or -1 if not present 
        all elements in the array are unique
        brute force: iterate through and find which index holds the target
        """

        l, r = 0, len(nums) - 1

        while l <= r: 
            mid = l + (( r - l) // 2)
            if nums[mid] == target:
                return mid
            
            #if sorted 
            if nums[l] <= nums[r]:
                if target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
             
            #if rotated
            else:
                if nums[l] <= nums[mid]:
                    #if left is sorted 
                    if nums[l] <= target <= nums[mid]:
                        r = mid - 1 #search left
                    else:
                        l = mid + 1 #search right
                else:
                    #if right is sorted 
                    if nums[mid] <= target <= nums[r]:
                        l = mid + 1 #search right 
                    else:
                        r = mid - 1 #search left
        return -1




        