class Solution:
    def numTrees(self, n: int) -> int:
        memo = {}

        def solve(n):
            if n <= 1:
                return 1
            
            if n in memo:
                return memo[n]
            
            res = 0 
            for i in range(1,n+1):
                L_count = solve(i-1)
                R_count = solve(n-i)
                res += L_count * R_count
            
            memo[n] = res
            return res
        return solve(n) 