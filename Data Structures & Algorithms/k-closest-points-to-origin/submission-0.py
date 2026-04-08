class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """ 
        points list = [[0,2], [2,2]]
        origin = [0,0]
        calculate the distance of each point to the origin 
        store them in a min heap
        for the range k: pop the top k
        """

        distance = []
        heapq.heapify(distance)
        res = []

        for i in points:
            dis = i[0]**2 + i[1]**2
            heapq.heappush(distance, (dis, i))

        while k > 0:
            res.append(heapq.heappop(distance)[1])
            k = k - 1
        
        return res




        
