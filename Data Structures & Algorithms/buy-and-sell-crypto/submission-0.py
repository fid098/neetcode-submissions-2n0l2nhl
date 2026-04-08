class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        """
        given an array prices where prices[i] is the price on the ith day
        we choose a single day to buy and choose a single day in the future to sell 

        we return the max profit 
        """

        res = 0
        buy = prices[0]

        for i in range(len(prices)):
            buy = min(buy, prices[i])
            profit = prices[i] - buy
            res = max(res, profit)

        return res


