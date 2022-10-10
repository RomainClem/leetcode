from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1: return 0 if nums[0] == target else -1
        
        mid = len(nums) // 2
        l, r, lorder = 0, mid, False
        l2, r2, rorder = mid, len(nums), False
        
        while True:
            if r-l in [0, 1] and r2-l2 in [0,1]:
                if nums[l] == target: return l
                elif nums[r] == target: return r
                else: return -1
            
            lorder = nums[l] <= nums[r-1]
            rorder = nums[l2] <= nums[r2-1]
            
            if lorder and rorder and target > nums[r2-1] and target < nums[l]: return -1 
            
            elif lorder and nums[l] <= target <= nums[r-1]: l, r, l2, r2 =  self.new_(l,r,l2,r2)
            elif rorder and nums[l2] <= target <= nums[r2-1]: l, r, l2, r2 = self.new_bucket(l2,r2, l, r)

            elif nums[r-1] >= target <= nums[r2-1]: 
                if nums[r-1] < nums[r2-1]: l, r, l2, r2 = self.new_bucket(l,r,l2,r2) 
                elif nums[r2-1] < nums[r]: l, r, l2, r2 = self.new_bucket(l2,r2, l, r)
            
            elif nums[l] <= target >= nums[l2]:
                if nums[l] > nums[l2]: l, r, l2, r2 =  self.new_bucket(l,r,l2,r2)
                elif nums[l2] > nums[l]: l, r, l2, r2 = self.new_bucket(l2,r2, l, r)
                
            else: return -1
            
            print(nums[l:r])
            print(nums[l2:r2])
                    
            
                
            
    def new_bucket(self, l,r,l2,r2):
        mid = (r-l) // 2
        l, r = l, l + mid
        l2, r2 = l+mid, r+mid
        return l, r, l2, r2
               

            
            
        
        
print(Solution().search([5,1,3], 0))
print(Solution().search([5,1,3], 1))
print(Solution().search([1,3,5], 3))
print(Solution().search([1,3,5], 1))
print(Solution().search([1,3,5], 0))
print(Solution().search([4,5,6,7,0,1,2], 0))
print(Solution().search([4,5,6,7,0,1,2], 3))
print(Solution().search([4,5,6,7,0,1,2], 7))
print(Solution().search([1,1], 0))