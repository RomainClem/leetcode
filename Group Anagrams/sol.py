from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1: return [strs]
        
        words: dict[List] = {}
        list_word_dict: List = []
        
        for word in strs:
            word_dict = self.get_word_dict(word)
            
            try:
                i = list_word_dict.index(word_dict)
                words[i].append(word)
            except ValueError as e:
                list_word_dict.append(word_dict)
                words[len(list_word_dict)-1] = [word]
            
        return words.values()

    def get_word_dict(self, word):
        dict_s = {}
        for char_s in word:
            if char_s in dict_s: dict_s[char_s] +=1
            else: dict_s[char_s] = 1
        return dict_s


strs = ["eat","tea","tan","ate","nat","bat"]
output = [["bat"],["nat","tan"],["ate","eat","tea"]]

sol = Solution().groupAnagrams(strs)
print(sol == output)