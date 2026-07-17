class TrieNode:
    def __init__(self):
        self.value = 0
        self.children = {}
        self.end_word = False

class MapSum:

    def __init__(self):
        self.root = TrieNode()
        self.key_val = {}

    def insert(self, key: str, val: int) -> None:
        delta = val - self.key_val.get(key,0)
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
                node.children[char].value += val
            else:
                node.children[char].value += delta
            node = node.children[char]
        node.end_word = True
        self.key_val[key] = val

    def sum(self, prefix: str) -> int:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.value
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)


"""
class MapSum:

    def __init__(self):
        self.count = {}
        

    def insert(self, key: str, val: int) -> None:
        self.count[key] = val
            
    def sum(self, prefix: str) -> int:
        len_prefix = len(prefix)
        res = 0
        for word in self.count:
            transformed_word = word[:len_prefix]
            if transformed_word == prefix:
                res += self.count[word]
        return res
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)

"""