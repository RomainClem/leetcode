import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0: return False
        elif x<10 and x>=0: return True
        num_d = math.floor(math.log10(x) + 1)
        for i in range(num_d//2):
            first = x//(10**(num_d-1))
            last = x-((x//10)*10)
            if first != last: return False
            x -= first * (10**(num_d-1))
            x = x//10
            num_d-=2
        return True    
            
            
            
print(Solution().isPalindrome(9999))