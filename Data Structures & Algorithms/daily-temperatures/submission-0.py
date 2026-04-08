class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  #pair: [temp, index]

        #i = index, t = temp
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                #while current t is greater than top of stack 
                stackT, stackI = stack.pop()
                #pop out the top temp, index
                res[stackI] = (i - stackI)
                #at the position in the stack, enter the distance between the current index and that index
            #else add to the stack 
            stack.append((t, i))
        return res