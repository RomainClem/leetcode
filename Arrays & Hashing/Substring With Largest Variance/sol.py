from numpy import char


class Solution:
    def largestVariance(self, s: str) -> int:
        if len(s) <=2: return 0
        variance = 0
        max_variance = 0
        
        c_1 = [s[0], 1]
        c_2 = [s[1], 1]
        
        for i in range(2, len(s)):
           if c_1[0] == s[i]: c_1[1] +=1
           elif c_2[0] == s[i]: c_2[1] +=1
           else:
               
           variance = max(c_1[1], c_2[1]) - min(c_1[1], c_2[1])
           
           
        
        return variance
    
print(Solution().largestVariance("abcde"))
print(Solution().largestVariance("aababbb"))