from collections import deque

from pip import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1: return ["()"]
        
        res = []
        stack = deque()
        for _ in range(n): stack.append("(")
        for _ in range(n): stack.append(")")
        
        
        while stack[-2]!= "(" and stack[1] != ")":
            res.append(''.join(stack))
            val = stack.pop()
            stack
        
        return res
    
def main():
    print(Solution().generateParenthesis(3))
    
main()