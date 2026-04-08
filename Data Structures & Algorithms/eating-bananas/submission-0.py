class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        integer array piles where piles[i] = number of banananes in the ith pile 
        integer h = number of hours to eat all bananas 
        bananas-per-hour eating rate = k

        """

        l, r = 1, max(piles)
        res = r  #this would work(the max it could be)

        while l <= r:
            k = (r + l) // 2
            hours = 0 
            for pile in piles:  #iterate through piles and divide by selected k
                hours += math.ceil(pile / k) #this rounds up the hour
            
            if hours <= h:
                res = min(res, k)  #update the result with the smaller k 
                r = k - 1  #look for a smaller result
            else:
                l = k + 1  #search the right side for a larger result
        return res

