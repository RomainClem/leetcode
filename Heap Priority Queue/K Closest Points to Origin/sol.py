from cmath import sqrt
from heapq import heapify, heappop
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k == len(points): return points
        res = []
        for i, point in enumerate(points):
            val = sqrt(point[0] ** 2 + point[1]**2).real
            points[i] = [val, point[0], point[1]]
        
        heapify(points)
        for _ in range(k):
            val = heappop(points)
            res.append([val[1], val[2]])
        
        return res

print(Solution().kClosest(points = [[1,3],[-2,2]], k = 1))
print(Solution().kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2))


# from cmath import sqrt
# from heapq import heapify, heappop, heappush
# from typing import List


# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         if k == len(points): return points
#         heap_q = []
#         res = []
#         for point in points:
#             val = sqrt(point[0] ** 2 + point[1]**2).real
#             heappush(heap_q, [val, point[0], point[1]])
        
#         for _ in range(k):
#             val = heappop(heap_q)
#             res.append([val[1], val[2]])
        
#         return res

# print(Solution().kClosest(points = [[1,3],[-2,2]], k = 1))
# print(Solution().kClosest(points = [[3,3],[5,-1],[-2,4]], k = 2))