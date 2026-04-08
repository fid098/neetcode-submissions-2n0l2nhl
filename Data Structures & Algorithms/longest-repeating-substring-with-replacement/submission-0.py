class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        given a string s consisting of only uppercase english chars
        given an integer k 
        we can choose up to k characters of the string
        and replace them with any other uppercase english characters

        after replacing them, we return the length of the longest substring 
        """

        count = {}
        res = 0 

        l = 0
        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0) #as we iterate through the list, we increment the freq of each element 
            maxf = max(maxf, count[s[r]])  #update the max frequency

            while (r - l + 1) - maxf > k:  #while the substring length - the max frequency is > k
                count[s[l]] -= 1  #we decrement the frequency of the left pointer
                l += 1  #and move the left pointer up
            res = max(res, r - l + 1)  #the result would be the distance between the right and left pointer 
        return res 