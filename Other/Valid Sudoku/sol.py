from sys import base_prefix
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for rows in board:
            row = []
            for char in rows:
                if char != ".": row.append(int(char))
            if len(set(row)) != len(row): return False
        
        
        for c in range(9):
            col = []
            for r in range(9):
                if board[r][c] != ".": col.append(int(board[r][c]))
            if len(set(col)) != len(col): return False
         
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                new_arr = board[i][j:3+j] +  board[i+1][j:3+j] + board[i+2][j:3+j]
                row = []
                for char in new_arr:
                    if char != ".": row.append(int(char))
                if len(set(row)) != len(row): return False           
        
        return True


board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

sol = Solution().isValidSudoku(board)

print(sol)