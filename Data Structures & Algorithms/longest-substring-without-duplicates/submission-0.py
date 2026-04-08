class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        given a string s 
        return the lenght of the longest substring without duplicate
        we could use a set to hold the substrings 

        if all substrings are the same letter, the length is 1
        """

        sub = set()
        length = 0 
        l = 0 

        for r in range(len(s)):
            while s[r] in sub:
                sub.remove(s[l])
                l += 1
            sub.add(s[r])
            length = max(length, r - l + 1)
        return length