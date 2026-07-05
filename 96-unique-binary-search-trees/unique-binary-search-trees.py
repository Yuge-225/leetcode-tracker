class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}
        
        def solve(n):
            if n <= 1:
                return 1
            
            if n in memo:
                return memo[n]
            

            res = 0 # res 表示我们有n个节点，最多可以组成多少种不同的BST树
            
            for i in range(1,n+1):
                left_tree = solve(i-1)
                right_tree = solve(n-i)
                res += left_tree * right_tree
            
            memo[n] = res
            return res
        return solve(n)