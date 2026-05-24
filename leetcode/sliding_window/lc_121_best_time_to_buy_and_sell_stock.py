from typing import List


'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we will first init our
        # buy price to (10^4)+1 because
        # the max price possible is 10^4
        buy_price = (10**4)+1

        # we will init our max profit to 0
        max_profit = 0

        # loop through all prices
        for i in range(len(prices)):
            # we want to minimize our buy price
            # if we find a lower buy price, then
            # we will store that as our optimal buy price
            buy_price = min(prices[i], buy_price)

            # we wil calculate our profit as the difference
            # between the buy price and the current price
            profit = prices[i] - buy_price
            # if the profit > max_profit, update max_profit
            max_profit = max(profit, max_profit)

        # finally, return the max profit
        return max_profit
