class Solution:
    def topKFrequent(self, words, k):
        freq = {}
        for word in words:
            freq[word] = freq.get(word,0) + 1
        
        all_words = freq.keys()

        res = sorted(all_words, key = lambda word: (-freq[word],word))
        return res[:k]