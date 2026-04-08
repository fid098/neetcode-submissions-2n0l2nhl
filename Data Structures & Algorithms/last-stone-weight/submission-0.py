class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #stones[i] = weight of ith stone
        #we could turn this into a maxheap 

        stones = [-s for s in stones]
        #makes every value in the array negative 
        #heapify would put the largest at the start 
        heapq.heapify(stones)

        while len(stones) > 1:
            first = abs(heapq.heappop(stones))
            second = abs(heapq.heappop(stones))
            if first > second:
                heapq.heappush(stones,  -(first - second))

        if stones:
            return -stones[0]
        return 0

    

        
