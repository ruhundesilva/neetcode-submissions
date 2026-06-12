class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        res = 0

        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
                continue
            diff = prices[i] - minPrice
            res = max(diff, res)
        return res