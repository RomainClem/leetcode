from collections import deque
from typing import List


class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        i = 0
        res = 0
        while i < len(strength):
            j = i
            arr = deque(strength[:i+1])
            
            while j < len(strength):
                res += sum(arr) * min(arr)
                j+=1
                arr.popleft()
                if j < len(strength): arr.append(strength[j])
                
            i+=1
        
        return res % (10 ** 9 + 7)
            
print(Solution().totalStrength([1,3,1,2,4,5,6,10000,1,2,3,4,5,6,7,8,8]))
# print(Solution().totalStrength([5,4,6]))
# print(Solution().totalStrength([747,812,112,1230,1426,1477,1388,976,849,1431,1885,1845,1070,1980,280,1075,232,1330,1868,1696,1361,1822,524,1899,1904,538,731,985,279,1608,1558,930,1232,1497,875,1850,1173,805,1720,33,233,330,1429,1688,281,362,1963,927,1688,256,1594,1823,743,553,1633,1898,1101,1278,717,522,1926,1451,119,1283,1016,194,780,1436,1233,710,1608,523,874,1779,1822,134,1984]))