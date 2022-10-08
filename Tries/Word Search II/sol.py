from collections import deque
from typing import List

class WordNode:
    def __init__(self, c, pos, adjacent) -> None:
        self.char = c
        self.pos = pos
        self.adjacent = adjacent
        self.used = 0
    

class Solution:
    def __init__(self) -> None:
        self.board = None
    
    def get_adjacent(self, row, col, condition):
        return [self.board[row][col], [row, col]] if 0 <= condition <= len(self.board[0])-1 else None
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        char_matrix: List[List[WordNode]] = []
        chars: dict[List[WordNode]] = {}
        self.board = board
        
        for row, word in enumerate(board):
            char_matrix.append([])
            for col, char in enumerate(word):
                
                adj_c = []
                adj_p = []
                
                up = self.get_adjacent(row-1, col, row-1) 
                if up: adj_c.append(up[0]); adj_p.append(up[1])
                
                left= self.get_adjacent(row, col-1, col-1)
                if left: adj_c.append(left[0]); adj_p.append(left[1])
                
                down = self.get_adjacent(row+1, col, row+1)
                if down: adj_c.append(down[0]); adj_p.append(down[1])

                right = self.get_adjacent(row, col+1, col+1)
                if right: adj_c.append(right[0]); adj_p.append(right[1])
 
                node = WordNode(char, [row, col], [adj_c, adj_p])
                char_matrix[row].append(node)
                
                if char not in chars: chars[char] = [node]
                else: chars[char].append(node)
        
        res = []
        for word in words:
            i = 0
            
            if word[0] not in chars: continue
            
            word_builder = deque()
            word_builder.append(deque())
            for node in chars[word[0]]:
                if node.used < 2: word_builder[0].append(node)
            
            while word_builder and i < len(word)-1:
                if word[i+1] not in word_builder[i][0].adjacent[0]: 
                    word_builder[i].popleft()
                    if len(word_builder[i]) == 0: 
                        word_builder.pop()
                        i-=1
                    continue
                
                node_list = deque()
                c_l = word_builder[i][0].adjacent
                
                for j, c in enumerate(c_l[0]):
                    if c == word[i+1] and char_matrix[c_l[1][j][0]][c_l[1][j][1]].used < 2:
                        node_list.append(char_matrix[c_l[1][j][0]][c_l[1][j][1]])
                
                word_builder.append(node_list) 
                i+=1
            
            
            if word_builder:
                for node_list in word_builder:
                    node_list[0].used += 1

                res.append(word)
        
        return res            
                    
                    
def main():
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]
    print(Solution().findWords(board, words))
    
main()