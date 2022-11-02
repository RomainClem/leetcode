from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if nums[0] > target > nums[-1]: return -1
        
        l, r = 0, len(nums) -1
        
        while l <= r:
            mid = (l + r) // 2
            val = nums[mid]
            
            if target == val: 
                return mid
            
            elif target > val: 
                l = mid+1
                
            else:
                r = mid-1
        
        return -1