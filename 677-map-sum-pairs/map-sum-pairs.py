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