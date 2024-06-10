# Question
"""You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 """

# Answer
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0

        min_prices = float('inf')
        max_prices = 0

        for price in prices:
            if price < min_prices:
                min_prices = price
            current_profit = price - min_prices
            if current_profit > max_prices:
                max_prices = current_profit

        return max_prices

