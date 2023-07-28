from collections import namedtuple

Value = namedtuple("Value", "min top")

class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(Value(min=val, top=val))
            return
        min_value = min(self.stack[-1].min, val)
        self.stack.append(Value(min=min_value, top=val))

    def pop(self) -> None:
        if self.stack:
            return self.stack.pop().top

    def top(self) -> int:
        if self.stack:
            return self.stack[-1].top

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1].min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()