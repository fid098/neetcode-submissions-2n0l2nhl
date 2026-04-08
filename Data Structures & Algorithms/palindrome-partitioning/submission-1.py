class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, sol = [], []

        def dfs(i):
            #if at the end of the tree 
            if i == len(s):
                res.append(sol[:])
                return 

            #loop through and check each for palindromes
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    sol.append(s[i : j + 1])
                    dfs(j + 1)
                    sol.pop()
            
        dfs(0)
        return res

    #helper function to check for palindrome
    def isPali(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i = i + 1
            j = j - 1

        return True

    