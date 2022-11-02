from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        if nums[0] > target > nums[-1]: return False
        
        l, r = 0, len(nums) -1
        
        while l <= r:
            mid = (l + r) // 2
            val = nums[mid]
            
            if target == val: 
                return True
            
            elif target > val: 
                l = mid+1
                
            else:
                r = mid-1
        
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l, r = 0, len(matrix) -1
        
        while l <= r:
            mid = (l + r) // 2
            arr = matrix[mid]
            
            if arr[0] <= target <= arr[-1]:
                return self.search(arr, target)

            elif target > arr[-1]:
                l = mid+1

            elif target < arr[0]:
                r = mid-1
                
            else:
                return False