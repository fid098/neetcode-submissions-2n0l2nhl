class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums #initialised as a heap
        self.k = k
        heapq.heapify(self.minHeap) #heapify the min heap
        while len(self.minHeap) > k: #if greater than k
            heapq.heappop(self.minHeap) #pop smallest

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        
