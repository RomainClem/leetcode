class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = maxc = 1 
        replace: int = 0
        prev: str = s[0]
        
        for c in s[1:]:
            if c == prev:
                count += 1
            
            elif replace < k:
                count += 1
                replace += 1
            else:
                maxc = max(count, maxc)
                count = 1
                replace = 0
                prev = c
                
        maxc = max(count, maxc)
        return maxc
                
            
            
        
print(Solution().characterReplacement("ABAB", 2))