class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 > 0: return False
        l_brackets = []
        for c in s:
            c = ord(c)
            
            if c in [41, 125, 93] and len(l_brackets) > 0:
                if c == 41:
                    if l_brackets[-1] == 40:
                        l_brackets.pop()
                    else: return False    
                            
                elif c == 125:
                    if l_brackets[-1] == 123:
                        l_brackets.pop()
                    else: return False    
                
                elif c == 93:
                    if l_brackets[-1] == 91:
                        l_brackets.pop()
                    else: return False
                    
            else: l_brackets.append(c)
        return len(l_brackets) == 0
    

print(Solution().isValid("()[]{}"))