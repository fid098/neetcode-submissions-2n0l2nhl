class Solution:
    def isValid(self, s: str) -> bool:
        """
        we will use a stack 
        map each closing bracket to an opening bracket 
        iterate through s, if a opening bracket, push to stack 
        if a closing bracket, check if the top of the stack is the mapping to the closing bracket 
        then pop 
        """

        stack = []
        mapping = {")":"(", "}":"{", "]": "["}

        for char in s:
            #check if char is a closing bracket
            if char in mapping:
                #check if stack is not empty
                #check if the last entry on the stack is the same as char
                if stack and stack[-1] == mapping[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
                
        return True if not stack else False
        #return if the stack is empty
            

        
                    


