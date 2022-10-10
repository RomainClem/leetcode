from collections import deque


class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        if val < self.min: self.min = val
        self.stack.append([val, self.min])

    def pop(self) -> None:
        self.stack.pop()
        if len(self.stack) > 0:
            self.min = self.stack[-1][1]
        else:
            self.min = float('inf')

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.min