from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        if len(nums) < k: return max(nums)
        
        window = deque(nums[:k])
        cur_max = max(window)
        maxs = [cur_max]
        
        for i in range(1, (len(nums)-k)+1):
            last = window.popleft()
            new = nums[(i+k)-1]
            window.append(new)
            
            if new >= cur_max:
                cur_max = new
            elif last == cur_max and new < cur_max:
                if window[0] == last-1: cur_max = window[0]
                else: cur_max = max(window)
            
            maxs.append(cur_max)()
        
        return maxs
            
            

def main():
    sol = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(sol.maxSlidingWindow(nums, k))
    print(sol.maxSlidingWindow([1], 1))
  
    # print(sol.maxSlidingWindow(big_ass_list, k))

main()
        