class Trie:

    def __init__(self):
        self.pt = {}

    def insert(self, word: str) -> None:
        pt = self.pt
        for c in word:
            if c not in pt:
                pt[c] = {}
            pt = pt[c]

        pt['.'] = '.'

    def search(self, word: str) -> bool:
        pt = self.pt
        for c in word:
            if c not in pt:
                return(False)
            pt = pt[c]
        
        return( '.' in pt )
        
    def startsWith(self, prefix: str) -> bool:
        pt = self.pt
        for c in prefix:
            if c not in pt:
                return(False)
            pt = pt[c]
        return(True)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)