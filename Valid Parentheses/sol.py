class Solution:
    def isValid(self, s: str) -> bool:
        dic_s = {}
        for c in s:
            c = ord(c)
            if c == 41:
                op = dic_s.get(40, 0)
                if op == 0: return False
                
            elif c == 125:
            elif c == 93: