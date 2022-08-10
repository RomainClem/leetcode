from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        min_v = prices.pop(0)
        for num in prices:
            if num < min_v:
                min_v = num
            output = max(num-min_v, output)
        
        return output
    
    
print(Solution().maxProfit([[7,1,5,3,6,4]])