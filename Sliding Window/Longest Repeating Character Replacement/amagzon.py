class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1: return 1
        l = 0
        res = 0
        word_dict = {}
        for i, c in enumerate(s):
            if c in word_dict and l <= word_dict[c]: 
                l = word_dict[c]+1
            else:
                res = max(res, i-l+1)
            
            word_dict[c] = i
            
        return res
    
print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("bbbbb"))
print(Solution().lengthOfLongestSubstring("pwwkew"))
print(Solution().lengthOfLongestSubstring("abcabcjhadlkfjhasflkhawefiouhwflihwuafeihawdfjhfhfhfhfhfbb"))
print(Solution().lengthOfLongestSubstring(""))
print(Solution().lengthOfLongestSubstring("au"))

