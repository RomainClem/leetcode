class Solution:
    def isPalindrome(self, s: str) -> bool:
        anagram = ""
        for c in s:
            if c.isalpha(): anagram += c.lower()
            elif c.isnumeric(): anagram += c
        
        if len(anagram) <= 1: return True

        for i in range(len(anagram) // 2):
            if anagram[i] != anagram[-(i+1)]: return False
        
        return True
    

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("race a car"))
print(Solution().isPalindrome(" "))
print(Solution().isPalindrome("0P"))
print(Solution().isPalindrome("abb"))