from collections import Counter

class Solution:

    def topKFrequent(self, words, k):

        count = Counter(words)

        # 频率降序，频率相同则字典序升序

        candidates = sorted(count.keys(), key=lambda w: (-count[w], w))

        return candidates[:k]