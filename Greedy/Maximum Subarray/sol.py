

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res, res_at = float("-inf"), 0
        
        for n in nums:
            res_at = res_at + n
            res = max(res, res_at)
            res_at = max(0, res_at)
    
        return res
    
    
print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))