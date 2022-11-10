from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) < 2: return nums[0]
        def helper(nums):
            s1 = 0
            s2 = 0

            for n in nums:
                temp = max(n+s1, s2)
                s1 = s2
                s2 = temp
            
            return s2
        
        return max(helper(nums[1:]), helper(nums[:-1]))