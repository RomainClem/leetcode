import re


class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        sum = 0
        for i, v in enumerate(s):
            if i+1 < len(s):
                sum = sum + roman[v] if roman[s[i+1]] <= roman[v] else sum - roman[v]
            else:
                sum += roman[v]
        
        return sum