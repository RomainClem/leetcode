from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        output = 0
        for r in range(1, len(prices)):
            if prices[r] < prices[l]: l = r
            
            output = max(output, prices[r]-prices[l])
        return output
    

print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit([2,1,4]))