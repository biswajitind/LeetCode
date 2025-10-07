class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = float('inf')

        # Brute Force: in this Time Limit Exceeds
        # because time Complexity is O(n^2)
        # for i in range(len(prices) - 1):
        #     for j in range(i+1, len(prices)):
        #         maxProfit = max(maxProfit, prices[j] - prices[i])
        # return(maxProfit)

        # Time complexity O(n), space complexity O(1)
        for price in prices:
            if price < minPrice:
                minPrice = price
            maxProfit = max(maxProfit, price - minPrice)
        return(maxProfit)




        