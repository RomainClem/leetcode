from pip import List


class Solution:
    

    def letterCombinations(self, digits: str) -> List[str]:
        res=[]
        if len(digits) ==0: return res
        
        dic: dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
                    
        self.dfs(digits, 0, dic, '', res)
        return res

    def dfs(self, nums, index, dic, path, res):
        if index == len(nums): return res.append(path)
        string1 = dic[nums[index]]
        for char in string1: self.dfs(nums, index+1, dic, path + char, res)
                
                
                
                
print(Solution().letterCombinations("237"))