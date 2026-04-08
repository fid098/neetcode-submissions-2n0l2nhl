class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False

        s_hashmap = {}
        t_hashmap = {}
        for i in s.lower():
            s_hashmap[i] = s_hashmap.get(i, 0) + 1
            #if i exists, return its current count or return 0 and increment 
        for j in t.lower():
            t_hashmap[j] = t_hashmap.get(j, 0) + 1

        if s_hashmap == t_hashmap:
            return True
        else:
            return False

        