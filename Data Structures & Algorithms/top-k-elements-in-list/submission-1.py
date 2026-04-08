class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #take in an array nums and int k
        #return the k most frequent elements within the array 
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
            #if num does not exist in the dictionary yet, default is 0
            #increments it by 1
        
        top_k = heapq.nlargest(k, count.keys(), lambda x : count[x])
        #find the top k largest elements
        #count.keys() is the iterables that is being checked 
        #lambda x: count[x] is the key that is used to compare the values 

        return top_k
        
