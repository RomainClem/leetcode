from collections import Counter, defaultdict
from typing import List

from numpy import sort


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)
        for s in strs:
            words[tuple(sorted(s))].append(s)
        return words.values()
        
        
print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(Solution().groupAnagrams(["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]))
print(Solution().groupAnagrams(["ddddddddddg","dgggggggggg"]))
