from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        bucket = 0
        l = [0,0]
        
        for i, v in enumerate(height):
            if v >= l[0]:
                l[0],l[1] = v, i
            