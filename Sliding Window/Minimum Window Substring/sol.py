from collections import Counter, deque

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        
        countT = {}
        for c in t: countT[c] = 1 + countT.get(c, 0)
    
        indexes = deque()
        res, reslen = [-1, -1], float("infinity")
        count = len(countT)
        l = 0
        
        for i, c in enumerate(s):
            if c in countT:
                indexes.append(i)
                countT[c] -= 1       
                if countT[c] == 0: count -= 1
                    
            while count == 0:
                if (i - indexes[l] + 1) < reslen: res, reslen = [indexes[l], i], i - indexes[l] + 1
                countT[s[indexes[l]]] += 1
                if countT[s[indexes[l]]] > 0: count += 1
                indexes.popleft()
                
        return "" if reslen > len(s) else s[res[0]: res[1]+1]
   

print(Solution().minWindow("cabwefgewcwaefgcf", "cae"))
print(Solution().minWindow("ADOBECODEBANC", "ABC"))
print(Solution().minWindow("a", "a"))
print(Solution().minWindow("a", "aa"))
print(Solution().minWindow("a", "b"))
print(Solution().minWindow("ab", "a"))