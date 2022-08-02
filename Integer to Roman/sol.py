class Solution:
    def intToRoman(self, num: int) -> str:
        
        roman_dict = {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
        }
        
        num_str = str(num)
        factor = 10 ** (len(num_str)-1)
        
        roman_num = ""
        
        for i in range(1, len(num_str)+1):
            
            ctoi = int(num_str[i-1])
            
            if ctoi < 4:
                roman_num += roman_dict[1 * factor] * ctoi
            elif ctoi == 4:
                roman_num += roman_dict[1 * factor] + roman_dict[5 * factor]
            elif ctoi < 9:
                roman_num += roman_dict[5 * factor] + (roman_dict[1 * factor] * (ctoi - 5))
            else:
                roman_num += roman_dict[1 * factor] + roman_dict[1 * (factor*10)]
                
            factor /= 10
            
        return roman_num
    
solution = Solution().intToRoman("3")