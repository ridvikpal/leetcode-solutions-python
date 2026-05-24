from functools import cache
from typing import List


'''
https://leetcode.com/problems/coin-change/description/
'''
class Solution:
    # we will use a top-down dynamic programming approach to solve this problem
    # by memoizing the result of a recursive function
    def coinChange(self, coins: List[int], amount: int) -> int:
        # our recursive (backtracking) search function
        # that attempts to create a total amount with
        # the least number of coins given to us
        # we use @cache to automatically memoize the result
        # of each function call
        @cache
        def search(total):
            # our first base case is when we reach a total of 0
            if total == 0:
                # this means we successfully created the
                # original amount, so return 0
                # no more coins are needed to create this value
                return 0

            # our second base case is when we reach a total less than 0
            if total < 0:
                # this means we did not successfully create the original amount
                # so return infinity to indicate this is a dead path
                # and using these coins the amount can never be made
                return float('inf')

            # set the minimum number of coins needed to create the total
            # to infinity at the start
            min_coins = float('inf')

            # loop through every coin
            for coin in coins:
                # update the minimum number of coins needed to create the total
                # if using this coin to decrease the total results in
                # less coins being needed
                min_coins = min(min_coins, search(total-coin))

            # finally, return the minimum number of coins needed + 1
            # because we use 1 coin to create the total at this iteration
            return min_coins + 1

        # search for the amount using our recursive search function
        result = search(amount)
        # only return the above result if it is not infinity
        # if it is infinity, then there is no way to create this amount
        # with the given coins, so return -1 instead
        return result if result != float('inf') else -1
