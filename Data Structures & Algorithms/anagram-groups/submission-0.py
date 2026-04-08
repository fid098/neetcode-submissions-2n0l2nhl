class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #key: value, charactercount: list of anagrams
        #defaultdict(list) creates an empty list when a key does not exist 


        for s in strs:
            count = [0] * 26 #holds 26 letters for checks a-z
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
            #since the count list cannot be a dictionary key 
            #make it a tuple which can be, and a tuple uniquely identifies an anagram group
            #if the key already exists, add the word to that group
        
        return list(res.values())
        #convert the dictionary values to a list return type 