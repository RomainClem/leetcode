class MinStack:

    def __init__(self):
        self.stack = [] #will consist of list of lists, with minimum at each point as second value

    def push(self, val: int) -> None:
        if (len(self.stack) == 0):
            self.stack.append([val, val]) 
        else:
            minValue = min(self.stack[-1][1], val)
            self.stack.append([val, minValue])

    def pop(self) -> None:
        self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]