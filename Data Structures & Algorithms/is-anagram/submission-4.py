class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26 
        #represents counts for letters a-z
        #initialized to zero at first 

        for i in range(len(s)):
            #for each index i, increment count for s and decrement count for t 
            count[ord(s[i]) - ord('a')] += 1
            #ord('a') returns the ascii number 
            #count[index of (ascii for current letter - ascii for a)] 
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True

 
        