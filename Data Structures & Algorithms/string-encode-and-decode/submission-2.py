class Solution:
    """
    encode "Hello World" = 5#Hello5#World

    decode 5#Hello5#World
    we have 3 pointers
    l,m,r at start, when l gets to num, put m at l + 2, put r at num + 1
    copy string m to r into list(str[m : r + 1])
    
    """

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        strs = []
        l = 0

        while l < len(s):
            m = l

            while s[m] != "#":
                m += 1

            length = int(s[l: m])

            word = s[m + 1: m + 1 + length]
            strs.append(word)

            l = m + 1 + length

        return strs