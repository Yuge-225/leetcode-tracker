class Solution:
    def numTrees(self, n: int) -> int:

        memo = {}

        def solve(n):
            if n <= 1:
                return 1
            
            if n in memo:
                return memo[n]
            res = 0
            for i in range(1,n+1,1):
                left_res = solve(i-1)
                right_res = solve(n-i)
                res += left_res*right_res
            
            memo[n] = res
            return res
        return solve(n)


















"""
class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}

        def solve(n):
            if n <= 1: # base case, 空树或者只有一个节点的树只有一种BST
                return 1
            
            if n in memo: #检查memo[n] 是否已经计算过，避免重复计算数据
                return memo[n]
            
            res = 0 # res 存储的就是给定n个节点，一共有多少种不同的BST树
            for i in range(1,n+1): #尝试每一个i值作为根节点
                L_count = solve(i-1) # 递归计算左，右子树
                R_count = solve(n-i)
                res += L_count * R_count # 左右子树组合
            
            memo[n] = res # 记录结果
            return res
        return solve(n) 

"""