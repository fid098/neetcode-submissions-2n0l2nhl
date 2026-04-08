class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False

        letter_count = {}

        for c in s:
            letter_count[c] = letter_count.get(c, 0) + 1

        for c in t:
            if c not in letter_count:
                return False
            letter_count[c] -= 1
            if letter_count[c] < 0:
                return False
        return True 
 
        