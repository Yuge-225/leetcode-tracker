class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True

    def search(self, word: str) -> bool:
        # 从根节点开始，处理 word 的第 0 个字符
        return self.dfs(self.root, word, 0)

    def dfs(self, curr_node, word, curr_index):
        # 终止条件：已经处理完 word 的所有字符
        # 检查当前节点是否是一个完整单词的结尾
        if curr_index == len(word):
            return curr_node.end_of_word
        
        curr_char = word[curr_index]  # 当前要处理的字符
        
        if curr_char == '.':
            # '.' 可以匹配任意字符
            # 遍历当前节点的所有子节点，逐个尝试
            for child_node in curr_node.children.values():
                # 用这个子节点继续处理下一个字符
                if self.dfs(child_node, word, curr_index + 1):
                    return True  # 只要有一条路径匹配，就返回 True
            return False  # 所有子节点都试过了，没有匹配的
        
        else:
            # 普通字符，直接找对应的子节点
            if curr_char not in curr_node.children:
                return False  # 当前字符不存在，匹配失败
            next_node = curr_node.children[curr_char]
            # 移动到下一个节点，处理下一个字符
            return self.dfs(next_node, word, curr_index + 1)