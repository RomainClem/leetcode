
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        target = float("infinity")
        
        while l <= r:
            mid = (l + r) // 2

            # left sorted portion
            if nums[l] <= nums[mid]:
                if nums[l] < target or target < nums:
                    target = min(nums[l], target)                
                    l = mid + 1
                else:
                    target = min(nums[r], target)
                    r = mid - 1
            # right sorted portion
            else:
                if nums[mid] < nums[r]: r = mid
                else: l = mid
            
        return target
    
print(Solution().findMin([3,1,2]))
print(Solution().findMin([3,4,5,6,7,8,1,2]))
print(Solution().findMin([5,1,2,3,4]))
print(Solution().findMin([2,3,4,5,1]))
print(Solution().findMin([4,5,6,7,0,1,2]))
print(Solution().findMin([3,4,5,1,2]))
print(Solution().findMin([11,13,15,17]))