import math
from typing import List


'''
https://leetcode.com/problems/coin-change/description/
'''
class Solution:
    # we will use a bottom up tabular dynamic programming
    # approach to solve this problem
    def coinChange(self, coins: List[int], amount: int) -> int:
        # first we start off by sorting our coins
        # in ascending order, because
        # this will allow us to easily break 
        # when we find a coin that is too large to use
        # to create an amount
        coins.sort()

        # init out min coins array for dynamic programming where
        # index -> money amount we want to create
        # value -> minimum number of coins to make that amount
        # we init all values to infinity because we don't know 
        # the number of coins it takes to make any amount yet
        # the length of this array is amount+1 because we want to know
        # how to create money amounts from $0 up to the amount
        min_coins = [math.inf]*(amount + 1)
        # our base case is making an amount of $0
        # which obviously takes 0 coins, so update
        # min coins accordingly
        min_coins[0] = 0

        # loop through all indices in the min coins
        # array, skipping index 0 since we already
        # updated our base case
        # this is effectively looping through all
        # amount values i from $1 up to the amount
        for i in range(1, len(min_coins)):
            # loop through all coins
            # since we will test making each
            # amount i with 1 extra coin of each type
            for coin in coins:
                # assume we use 1 extra coin to create
                # the amount i
                # then calculate how much money we are missing
                # to create amount i (i.e., the difference)
                difference = i - coin
                
                # if the difference is negative that means
                # our coin value is too large to create the amount i
                # so there's no point in checking larger coins
                # remember our coins array is sorted in ascending order
                if difference < 0:
                    # break direclty out of the for loop
                    # and begin checking next amount value i
                    break
                
                # otherwise, update our min coins array
                # with the minimum of whatever value is currently stored
                # or 1 + the minimum number of coins to create the difference
                # we add 1 because we assumed using 1 extra coin to create
                # the amount i when calculating the difference
                min_coins[i] = min(min_coins[i], 1 + min_coins[difference])

        # finally, we will return the minimum number of coins it takes to
        # make the amount provied as input as long as it is not infinity
        # if it is infinity, we return -1 because the amount cannot
        # be created using the coins provided.
        return min_coins[amount] if min_coins[amount] != math.inf else -1
