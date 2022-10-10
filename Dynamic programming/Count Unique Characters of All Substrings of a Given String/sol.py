from collections import deque
from typing import Counter


class Solution:
    def uniqueLetterString(self, s: str) -> int:
        
        res = len(s)
        j = 2
        
        arr = deque(s[:j])
        unique = Counter(arr)
        
        count = 0
        for k, v  in unique.items(): 
            if v == 1: count += 1
        
        while j < len(s):
            
            for c in range(j-1, len(s)):
                new_count = count
                prev = arr.popleft()
                arr.append(s[c+1])
                
                prev_val = unique.get(prev)
                if prev_val == 1: new_count -= 1
                unique[prev] = prev_val - 1
                
                next_val = unique.get(s[c+1], 0)
                if next_val == 0: new_count += 1
                unique[s[c+1]] = next_val + 1
            
            res += count
            j+=1
            
            
        return res
    
print(Solution().uniqueLetterString("ABC"))