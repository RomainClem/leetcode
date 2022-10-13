from cgitb import small
from heapq import heapify, heappop, heappush, heappushpop
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heap = []
        for n in nums:
            if len(heap) != k: heappush(heap, n)
            else: heappushpop(heap, n)
            
        self.num = heap 

    def add(self, val: int) -> int:
        if len(self.num) != self.k: heappush(self.num, val)
        else: heappushpop(self.num, val)
        return self.num[0]
    
    
test = KthLargest(3, [4, 5, 8, 2])
print(test.add(3))