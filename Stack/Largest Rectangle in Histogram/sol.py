from collections import Counter, OrderedDict, deque
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        q = deque(heights)
        max_height = 0
        counter = Counter(heights)
        counter = OrderedDict(sorted(counter.items()))
        
        while len(q) > 1:
            max_height = max(len(q) * next(iter(counter)), max_height) 
            if q[0] < q[-1] or q[-1] < q[0]:
                val = q.popleft() if q[0] < q[-1] else q.pop()
                counter[val] -= 1
                if counter[val] == 0: counter.pop(val)

            elif len(counter) > 1:
                min_val = next(iter(counter))
                for i in range(len(q)):
                    if q[i] == min_val:
                        for _ in range(i+1):
                            val = q.popleft()
                            counter[val] -= 1
                            if counter[val] == 0: counter.pop(val)
                        break

                    elif q[-(i+1)] == min_val:
                        for _ in range(i+1):
                            val = q.pop()
                            counter[val] -= 1
                            if counter[val] == 0: counter.pop(val) 
                        break
            else:
                break
            
        return max(q[0], max_height)
    
# print(Solution().largestRectangleArea([2,1,5,6,2,3]))
# print(Solution().largestRectangleArea([4,2,0,3,2,4,3,4]))
print(Solution().largestRectangleArea([5,5,1,7,1,1,5,2,7,6]))
