
from collections import defaultdict, deque
import queue
from tkinter import N
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if len(prerequisites) < 1: return True
        courses = defaultdict(set)
        indeg = [0] * numCourses
        
        for key, value in prerequisites:
            # if key == value: return False
            
            courses[value].add(key)
            indeg[key] += 1

        queue = deque([i for i in range(numCourses) if indeg[i] == 0])
        
        res = 0
        while queue:
            cur = queue.popleft()
            res +=1
            for val in courses[cur]:
                indeg[val] -= 1
                
                if indeg[val] == 0: queue.append(val)
       
        return res == numCourses
        

# print(Solution().canFinish([[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]))
# print(Solution().canFinish(5, [[1,4],[2,4],[3,1],[3,2]]))
print(Solution().canFinish(3, [[1,0],[1,2], [0,1]]))
# print(Solution().canFinish(2, [[1,0],[1,2],[0,1]]))