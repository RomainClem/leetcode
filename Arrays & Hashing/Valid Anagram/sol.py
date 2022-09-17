class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        dict_s, dict_t = {}, {}
    
        for char_s in s:
            if char_s in dict_s: dict_s[char_s] +=1
            else: dict_s[char_s] = 1
            
        for char_t in t:
            if char_t not in dict_s: return False
            if char_t in dict_t:
                dict_t[char_t] += 1
                if dict_t[char_t] > dict_s[char_t]: return False
            else: dict_t[char_t] = 1
            
        return True
