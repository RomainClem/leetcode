from asyncio import proactor_events
import enum
from itertools import count
import webbrowser
from pip import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        seq = 1
        counter = set(nums)
        
        while True:
            num = counter.pop()
            prev_num = num - 1
            next_num = num + 1
            new_seq = 1
            while True:
                if prev_num in counter:
                    new_seq +=1
                    counter.remove(prev_num)
                    prev_num -= 1
                elif next_num in counter:
                    new_seq += 1
                    counter.remove(next_num)
                    next_num += 1
                else:
                    break                
            
            seq = max(seq, new_seq)
            if seq >= len(counter): return seq
            
            
    
                

nums = [0,3,7,2,5,8,4,6,0,1]

sol = Solution().longestConsecutive(nums)

print(sol)
