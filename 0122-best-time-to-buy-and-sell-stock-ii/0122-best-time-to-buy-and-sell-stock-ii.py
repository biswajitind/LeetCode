class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Since we are not allowed to hold for more than one day, it means yesterdays price is the buying price.
        profit = 0
        buyAt = prices[0]
        for i in range(1, len(prices)):
            profit += max(0, prices[i] - buyAt)
            buyAt = prices[i]
        
        return(profit)

        