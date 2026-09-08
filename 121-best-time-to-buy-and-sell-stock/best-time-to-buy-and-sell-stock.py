class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        purchase_price = float("inf")
        max_profit = 0
        for price in prices:
            if price < purchase_price:
                purchase_price = price
            if max_profit < price - purchase_price:
                max_profit = price - purchase_price
        return max_profit




