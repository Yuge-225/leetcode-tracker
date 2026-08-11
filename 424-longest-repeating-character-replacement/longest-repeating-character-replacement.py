class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left,right = 0,0
        window = {}
        longest = 0
        while right < len(s):
            c = s[right]
            right += 1
            window[c] = window.get(c,0) + 1
            most_freq = max(window.values())


            while (right - left) - most_freq > k:

                d = s[left]
                left += 1
                window[d] -= 1
                most_freq = max(window.values())

            longest = max(longest,right-left)

        return longest




