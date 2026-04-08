class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = [] #empty list
        i = 0  #pointer at the start of the string
        j = 0

        while i < len(s): #while the pointer is not at the end of the string
            j = i #another pointer at the start 
            while s[j] != "#":  #while the j pointer is not at #
                j = j + 1  #j pointer moves to the next character
            length = int(s[i:j])  #the length is the value of the i(at the start) up until and not including j so i 
            res.append(s[j + 1: j + 1 + length]) #we append (j(at #) + 1)first letter of word until last letter of word 
            i =  j + 1 + length #increment the i pointer to the next digit
        return res