class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = {}
        left,right =0, 0
        res = 0
        while right < len(s):
            c = s[right]
            right += 1
            window[c] = window.get(c,0) + 1
            
            while window[c] > 1: # 如果新加入的右边界字符已经在出现在滑动窗口里了
                d = s[left] # 从最左边界开始一个一个收缩窗口
                left += 1 
                window[d] = window.get(d,0) - 1
            # 出了while循环表示当前窗口内的字符已经合法（不含重复字符）
            res = max(res,right-left)

        return res
            