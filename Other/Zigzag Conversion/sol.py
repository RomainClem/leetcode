def create_full_col( string_i, s, numRows, matrix, col_check):
    for i in range(numRows):    
        if string_i == len(s): break                
        matrix[i].append(s[string_i])
        string_i += 1
    col_check += 1
    return col_check, string_i

def create_zig_zag_col( numRows, zz_row, s, string_i, matrix, col_check):
    for i in range(numRows):
        c_ins = s[string_i] if i == zz_row else ""
        matrix[i].append(c_ins)            
    string_i+=1
    col_check += 1
    zz_row -=1
    return string_i, col_check, zz_row 
        
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) <= numRows: return s
        string_i = col_check = 0

        zz_row = numRows-2
        matrix = [[] for x in range(numRows)]
        
        while True:
            if string_i == len(s): break
            if col_check == 0 or numRows-2 == 0: col_check, string_i = create_full_col(string_i, s, numRows, matrix, col_check)
            elif col_check <= numRows // 2: string_i, col_check, zz_row = create_zig_zag_col(numRows, zz_row, s, string_i, matrix, col_check)
            else:
                col_check = 0
                zz_row = numRows-2

        # print(matrix)
        output = []    
        for arr in matrix: output += arr
        return "".join(output)
        
            
sol = Solution()
print(sol.convert("PAYPALISHIRING", 5))


#Terrible and doesn't work