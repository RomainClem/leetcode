class Solution:
    def fib(self, n: int) -> int:
        
        fib =  [0, 1]
        if n<2: return fib[n]
        
        for _ in range(2, n+1):
            temp = fib[0] + fib[1]
            fib[0] = fib[1]
            fib[1] = temp
        return fib[1]

