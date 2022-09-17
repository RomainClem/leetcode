import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
            
        return ans.values()


strs = ["eat","tea","tan","ate","nat","bat"]
output = [["bat"],["nat","tan"],["ate","eat","tea"]]

sol = Solution().groupAnagrams(strs)
print(sol == output)