import re
from string import ascii_lowercase


class Solution:
    def largestVariance(self, s: str) -> int:
        
        def kadane(a, b):
            ans = 0
            countA, countB = 0, 0
            canExtendPrevB = False
            
            for c in s:
                if b != c != a: continue
                
                if c == a: countA += 1
                else: countB += 1
                
                if countB > 0: ans = max(ans, countA-countB)
                elif countB == 0 and canExtendPrevB: ans = max(ans, countA-1)
                
                if countB > countA:
                    countA = 0
                    countB = 0
                    canExtendPrevB = True
                    
            return ans
        
        ans = 0
        for c1 in ascii_lowercase:
            for c2 in ascii_lowercase:
                if c1 != c2: ans = max(ans, kadane(c1,c2))
                
        return ans