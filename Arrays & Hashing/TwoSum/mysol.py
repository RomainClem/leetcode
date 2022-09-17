
import enum


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    nums_dict = {}
    for i in range(len(nums)):
        if nums[i] in nums_dict:
            nums_dict[nums[i]].append(i)
        else:
            nums_dict[nums[i]] = [i]
            
    for i in range(len(nums)):
        num_target = target - nums[i]
        if num_target in nums_dict:
            if num_target == nums[i] and len(nums_dict[num_target])>1:
                return [i, nums_dict[num_target][1]]
            elif num_target != nums[i]:
                return [i, nums_dict[num_target][0]]

output = twoSum([2, 7, 11, 15], 9)
# output = twoSum([3,2,4], 6)
print(output)