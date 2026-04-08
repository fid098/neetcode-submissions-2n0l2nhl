class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        res = []

        def backtrack(i, cur, total):
            if total == target:
                res.append(cur[:])
                return 
            
            if i >= n or total > target:
                return 

            for j in range(i, n):
                #check if it is a duplicate
                #if not a duplicate
                
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                
                cur.append(candidates[j])
                backtrack(j + 1, cur, total + candidates[j])
                cur.pop()
        
        backtrack(0, [], 0)
        return res
        
                

