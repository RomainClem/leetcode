from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        col = Counter(s1)
        cur = {}
        char_count = 0
        j = -1
        if len(s1) > len(s2): return False
        
        for i, c in enumerate(s2):
            
            if c in col:
                if j == -1: j = i
                cur[c] = cur.get(c, 0)+1
                
                while cur[c] > col[c]:
                    cur[s2[j]] -= 1
                    j += 1
                    char_count -= 1
                
                char_count+=1
                if char_count == len(s1): return True
            
            else:
                char_count = 0
                cur = {}
                j=-1
                
        return False
        
def main():
    print(Solution().checkInclusion("ab", "eidbaooo"))
    print(Solution().checkInclusion("ab", "eidboaoo"))
    print(Solution().checkInclusion("adc", "dcda"))
    print(Solution().checkInclusion("dinitrophenylhydrazine", "acetylphenylhydrazine"))
    print(Solution().checkInclusion("rokx", "otrxvfszxroxrzdsltg"))
    print(Solution().checkInclusion("hello", "ooolleoooleh"))
    
main()