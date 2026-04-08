class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        initialise a stack
        depending on the operation, pop the last 2 items in the stack
        perform the operation and push to the stack 
        at the end return the only value in the stack 
        """

        stack = []

        for char in tokens:
            if char == "+":
                stack.append(stack.pop() + stack.pop())
                #push the result of the addition of the last two popped values 
            elif char == "-":
                a, b = stack.pop(), stack.pop()
                #a = second value
                #b = first value, we want b - a
                stack.append(b - a)
            elif char == "*":
                stack.append(stack.pop() * stack.pop())
                #push the result of the multiplication of the last two popped values 
            elif char == "/":
                a, b = stack.pop(), stack.pop()
                #a = second value
                #b = first value, we want b - a 
                #int(b - a) so it always truncates towards zero 
                stack.append(int(b / a))
            else:
                #if not an operation, it is a number so push to stack 
                stack.append(int(char))

        #return the only value in the stack 
        return stack[-1]
