from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        bucket = 0
        l, r = [height[0],0], [height[-1], len(height)-1]

        while l[1] != r[1]:
            
            if l[0] <= r[0]:
                l[1] += 1
                if height[l[1]] < l[0]: bucket += l[0] - height[l[1]]
                else : l[0] = height[l[1]]
            
            else:
                r[1] -= 1
                if height[r[1]] < r[0]: bucket += r[0] - height[r[1]]
                else : r[0] = height[r[1]]
        
        return bucket
    

# print(Solution().trap([4,2,0,3,2,5]))
print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))