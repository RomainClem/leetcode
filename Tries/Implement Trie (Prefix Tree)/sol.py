class Trie:

    def __init__(self):
        self.words = {}
        self.prefix = {}
        
    def insert(self, word: str) -> None:
        self.words[word] = 0
        pre = "" 
        for c in word:
            pre += c
            self.prefix[pre] = 0

    def search(self, word: str) -> bool:
       return word in self.words

    def startsWith(self, prefix: str) -> bool:
       return prefix in self.prefix


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)