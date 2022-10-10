class Solution:
    def isValid(self, s: str) -> bool:
        parantheses = {"(": ")", "{": "}", "[":"]"}
        
        stack = []
        for p in s:
            if p in parantheses: stack.append(p)
            elif len(stack) > 0:
                p_val = stack.pop()
                if p != parantheses[p_val]: return False
            else: return False
            
        return len(stack) == 0