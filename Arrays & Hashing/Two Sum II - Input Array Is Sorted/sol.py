from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num_dic: dict[int] = {}
        for i, v in enumerate(numbers):
            if target-v in num_dic: return [num_dic[target-v]+1, i+1]
            else: num_dic[v] = i