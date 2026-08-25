class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,root_word):
        node = self.root
        for char in root_word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.endOfWord = True

    def search_prefix(self,word):
        node = self.root
        prefix = ""
        for char in word:
            if char not in node.children:
                return word
            else:
                node = node.children[char]
                prefix += char
                if node.endOfWord:
                    return prefix
        return word
        

            
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for root_word in dictionary:
            trie.insert(root_word)
        res = []
        for word in sentence.split():
            transformed_word = trie.search_prefix(word)
            res.append(transformed_word)
        return " ".join(res)

"""

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
        
        在Trie中找每一个word的最短词根
        找到返回词根，找不到返回原单词
    
        node = self.root
        prefix = "" # 记录走过的字符，也就是当前匹配的前缀
        for char in word:
            if char not in node.children:
                return word # 如果当前字符不在Trie里，说明没有匹配词根，直接返回原单词
            node = node.children[char] #移动到下一个节点
            prefix += char #更新走过的字符串
            if node.end_of_word: # 找到词根结尾，返回最短匹配前缀
                return prefix 
        return word #走完单词所有字符，没找到词根，返回原单词

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        # 1. 构建Trie，把所有词根插入
        trie = Trie()
        for root_word in dictionary:
            trie.insert(root_word)
        # 2. 对句子每个单词，找最短匹配词根
        res = []
        for word in sentence.split(): ## 按空格分割成单词列表
            res.append(trie.search_prefix(word))    
        # 3. 拼接结果
        return " ".join(res)
"""