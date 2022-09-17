from ast import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix: str = ""
        if len(strs) == 1: return strs[0]
        last_word = strs.pop()
        
        for index, char in enumerate(last_word):
            for word in strs:
                if index == len(word) or word[index] != char: return prefix
            prefix += char
        
        return prefix