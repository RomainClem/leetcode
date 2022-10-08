from curses.ascii import isalpha
from math import fabs


class WordDictionary:

    def __init__(self):
        self.words = {}

    def addWord(self, word: str) -> None:
        self.words[word] = 0

    def search(self, word: str) -> bool:
        if word.isalnum(): return word in self.words
        
        for key in self.words.keys():
            if len(key) != len(word): continue
            
            for i, c in enumerate(word):
                if c != "." and c != key[i]: break
                if i == len(key)-1: return True
                
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)