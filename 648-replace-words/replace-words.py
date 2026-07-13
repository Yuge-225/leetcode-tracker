class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        node = self.root
        for char in word:
            if  char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True

    def search_prefix(self,word):
        node = self.root
        prefix = ""
        for char in word:
            if char not in node.children:
                return word
            node = node.children[char]
            prefix += char
            if node.end_of_word:
                return prefix
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()

        for word in dictionary:
            trie.insert(word)
        res = []
        for word in sentence.split():
            res.append(trie.search_prefix(word))    
        return " ".join(res)