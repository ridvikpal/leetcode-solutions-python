from functools import cache
import math
from typing import List


'''
https://leetcode.com/problems/coin-change/description/
'''
class Solution:
    # we will use a top down dynamic programming approach
    # by memoizing a recursive function to solve this problem
    def coinChange(self, coins: List[int], amount: int) -> int:
        # create our recursive (backtracking) function
        # it will find the minimum number of coins to create
        # a given amount
        # we will use @cache to automatically memoize the function outputs
        @cache
        def search(index, amount):
            # our first base case is when
            # our amount is 0. This means we
            # have a valid solution
            if amount == 0:
                # we can simply return 0,
                # since we are not selecting any more coins
                return 0

            # our second base case is when
            # our amount < 0 or the index is
            # out of bounds. This means we have 
            # an invalid solution
            if amount < 0 or index >= len(coins):
                # we can return infinity to indicate
                # that there is no minimum number of
                # coins along this combination 
                return math.inf
            
            # we can recursively explore all combinations
            # by testing 2 decision:
            # 1) choosing this coin, so add 1 to the recursion stack
            #    and reduce amount by this coin value
            # 2) skipping this coin, so just go to the next index
            choose_this_coin = 1 + search(index, amount-coins[index])
            skip_this_coin = search(index+1, amount)

            # we will return the value of the decision that gives
            # the minimum answer
            return min(choose_this_coin, skip_this_coin)

        # we will call our search function with
        # starting index 0 and amount
        min_coins = search(0, amount)

        # we will return the minimum coins or we will return 
        # -1 if our search function returns infinity
        return min_coins if min_coins != math.inf else -1
