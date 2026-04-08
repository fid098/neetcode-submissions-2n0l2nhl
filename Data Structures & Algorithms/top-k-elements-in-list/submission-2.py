class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}      

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        #top_k = heapq.nlargest(k, count.keys(), lambda x : count[x])

        maxheap = []
        for n in count.keys():
            maxheap.append([-(count[n]), n])

        heapq.heapify(maxheap)

        top_k = []
        for n in range(k):
            top_k.append(heapq.heappop(maxheap)[1])
        
        return top_k

        