from pip import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        for left in range(len(nums) - 2): # renamed this to left because this will always be the leftmost pointer in the triplet
            if left > target and nums[left] == nums[left - 1]: # this step makes sure that we do not have any duplicates in our result output
                continue 
            left2 = left + 1
            mid = left + 2 # renamed this to mid because this is the pointer that is between the left and right pointers
            right = len(nums) - 1
            while mid < right:
                cur_array = [[nums[left], nums[left2], nums[mid], nums[right]]]
                curr_sum = nums[left] + nums[left2] + nums[mid] + nums[right]
                if curr_sum < target:
                    mid += 1 
                elif curr_sum > target:
                    right -= 1
                else:
                    result.append([nums[left], nums[left2], nums[mid], nums[right]])
                    while mid < right and nums[mid] == nums[mid+1]: # Another conditional for not calculating duplicates
                        mid += 1
                    while mid < right and nums[right] == nums[right - 1]: # Avoiding duplicates check
                        right -= 1
                    mid += 1
                    right -= 1
        return result
    
sol = Solution().fourSum([1,0,-1,0,-2,2], 0)

print(sol)