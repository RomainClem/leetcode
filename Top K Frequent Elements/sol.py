from re import L
from pip import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count: dict = {}
        freq: List = [[] for i in range(len(nums) + 1)]
        for num in nums: count[num] = 1 + count.get(num, 0)
        for n, c in count.items(): freq[c].append(n) # highest count can't be greater than nums list size
        
        res = []
        for i in range(len(freq) - 1, 0, -1): # itterate from the end 
            for n in freq[i]: res.append(n)
            if len(res) == k: return res
            
    
nums, k = [1,1,1,2,2,3], 2

sol = Solution().topKFrequent(nums, k)

print(sol)