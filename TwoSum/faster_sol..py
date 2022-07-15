def twoSum(nums, target):
       seen = {}
       for i, value in enumerate(nums):
           remaining = target - nums[i]
           
           if remaining in seen:
               return [i, seen[remaining]]
            
           seen[value] = i
           
output = twoSum([2, 7, 11, 15], 9)
# output = twoSum([3,2,4], 6)
print(output)