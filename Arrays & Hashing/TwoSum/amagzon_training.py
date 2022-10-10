class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        
        for i, n in enumerate(nums):
            dif = target - n
            if dif in num_dict: return [i, num_dict[dif]]
            num_dict[n] = i