def check_negative(s, integers, char_i, s_builder):
    res = False
    while char_i < len(s):
        if s[char_i] in ["-", "+"] or s[char_i] in integers:
            if s[char_i] in ["-", "+"] and char_i+1 == len(s): return 0,0, False
            elif s[char_i] in ["-", "+"] and s[char_i+1] not in integers: return 0,0, False
            res = s[char_i] in integers
            s_builder += s[char_i]
            char_i += 1
            break
        elif s[char_i] == " ":
            char_i += 1
            continue
        else: return 0, 0, 0
    return char_i, s_builder, res
    
def build_int(s, integers, char_i, s_builder, res):
    if char_i == len(s) and not res: return 0, res
    while char_i < len(s):
        if s[char_i] in integers: s_builder += s[char_i]; res = True
        else: break
        char_i +=1
    return s_builder, res
    
class Solution(object):
    def myAtoi(self, s: str) -> int:
        if len(s) == 0: return 0
        integers: list[str] = ["0","1","2","3","4","5","6","7","8","9"]
        char_i: int = 0
        s_builder: str = ""
        char_i, s_builder, int_found = check_negative(s, integers, char_i, s_builder)
        if s_builder == 0: return 0
        s_builder, int_found = build_int(s, integers, char_i, s_builder, int_found)
        if not int_found: return 0
        s_to_i = int(s_builder)
        if s_to_i <= -2147483648: return -2147483648
        elif s_to_i >= 2147483647: return 2147483647
        return s_to_i

sol = Solution()
print(sol.myAtoi("+"))