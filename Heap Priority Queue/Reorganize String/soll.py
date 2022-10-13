from heapq import heapify, heappop, heappush
from typing import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        s = Counter(s)
        heap = [[-value, key] for key,value in s.items()]
        heapify(heap)
        res = [""]
        while len(heap) > 1:
            a = heappop(heap)
            b = heappop(heap) 
            
            if res[-1] == a[1]:
                res.append(b[1])
                res.append(a[1])
            else:
                res.append(a[1])
                res.append(b[1])
                
            a[0] += 1
            b[0] += 1
            
            if a[0] != 0: heappush(heap, a)
            if b[0] != 0: heappush(heap, b)
            
        if len(heap) > 0:
            a = heappop(heap) 
            a[0] += 1
            res.append(a[1])   
            
        return "".join(res) if a[0] == 0 else ""
            

print(Solution().reorganizeString("aabaaabccc"))
print(Solution().reorganizeString("aab"))