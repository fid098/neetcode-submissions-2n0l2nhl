class MinStack:
    """
    whenever we push to the stack, we push to another stack the minimum value at that moment
    whenever we pop, we pop from both stacks 
    whenever we return the top, we return the top of the main stack
    whenever we return the getmind, we return the top of the main stack
    """
    def __init__(self):
        self.stack = []
        self.Minstack = []
    
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.Minstack:
            val = min(val, self.Minstack[-1])
            self.Minstack.append(val)
        else:
            self.Minstack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.Minstack.pop()

    def top(self) -> int:
        return self.stack[-1]      

    def getMin(self) -> int:
        return self.Minstack[-1]

