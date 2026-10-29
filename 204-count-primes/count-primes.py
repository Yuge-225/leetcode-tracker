import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        # 先假设所有数字都是质数
        is_prime = [True] * n
        is_prime[0] = False
        is_prime[1] = False

        # 遍历所有数字
        for i in range(2,n):
            if is_prime[i]:
                # 排除i的所有倍数
                for j in range(i * i,n,i):
                    is_prime[j] = False
        return sum(is_prime)