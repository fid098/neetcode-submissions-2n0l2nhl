class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:


        minheap = []
        heapq.heapify(minheap)

        for i in range(len(nums)):
            heapq.heappush(minheap, nums[i])
            if len(minheap) > k:
                heapq.heappop(minheap)

        return minheap[0]
        


        
