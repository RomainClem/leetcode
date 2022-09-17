from re import S


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p_lookup: str = ""
        reg_ex: list[str] = ['.', '*']
        for c in p:
            if c in reg_ex:
                ''''''
                

sol = Solution()
print(sol.isMatch("aa", "a"))
print(sol.isMatch("aa", "a*"))
print(sol.isMatch("ab", ".*"))