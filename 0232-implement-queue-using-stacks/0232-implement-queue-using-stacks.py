class MyQueue:

    def __init__(self):
        self.push_stack = []
        self.pop_stack = []
        
    def push(self, x: int) -> None:
        self.push_stack.append(x)
        
    def pop(self) -> int:
        if len(self.pop_stack):
            return(self.pop_stack.pop())
        for i in range(len(self.push_stack)):
            self.pop_stack.append(self.push_stack.pop())
        if len(self.pop_stack):
            return(self.pop_stack.pop())
        return(None)   

    def peek(self) -> int:
        if len(self.pop_stack):
            return(self.pop_stack[-1])
        for i in range(len(self.push_stack)):
            self.pop_stack.append(self.push_stack.pop())
        if len(self.pop_stack):
            return(self.pop_stack[-1])
        return(None)   

    def empty(self) -> bool:
        return(not len(self.push_stack) + len(self.pop_stack))
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()