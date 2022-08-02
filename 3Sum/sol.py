from typing import List



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums_set: list = list(set(nums))
        nums_set.sort()
        nums_dict: dict = {}
        for i in nums:
            if i in nums_dict: nums_dict[i] += 1
            else: nums_dict[i] = 1
        print(nums_set)

        
        
        
        
Solution().threeSum([-1,0,1,2,-1,-4])




#   def threeSum(self, nums: List[int]) -> List[List[int]]:
        
#         triplets_set: List[set[int]] = []
#         triplets_list: list[list[int]] = []
        
#         for i, num1 in enumerate(nums):
#             for j, num2 in enumerate(nums):
#                 if j == i: continue
#                 for k, num3 in enumerate(nums):
#                     if i == k or k == j: continue
#                     if (num1 + num2 + num3) == 0 and {num1, num2, num3} not in triplets_set:
#                         triplets_set.append({num1, num2, num3})
#                         triplets_list.append([num1, num2, num3])
        
#         return triplets_list
 