from functools import cache
from typing import List


'''
https://leetcode.com/problems/coin-change-ii/description/
'''
class Solution:
    # we will use a top-down dynamic programming approach
    # by memoizing a recursive function to solve this problem
    def change(self, amount: int, coins: List[int]) -> int:
        # we can define our recursive (backtracking) search
        # function that searches through all possible combinations
        # of coins and keeps count of the ones that make up the amount
        # we will use @cache for automatic memoization
        @cache
        def search(index, amount):
            # our first base case is when we have
            # reached an amount of 0
            if amount == 0:
                # in this case we have found a valid
                # combination of coins that creates the amount
                # so return 1 for 1 combination found
                return 1

            # our second base case is if our index goes out
            # of bounds or our amount becomes negative
            if index >= len(coins) or amount < 0:
                # in this case this is not a valid combination
                # of coins and cannot create the amount
                # so return 0 for 0 combinations found
                return 0
            
            # finally, we can return the sum of the combinations
            # found by using 2 decisions on each recursion step:
            # 1) use this coin at index specifically and decrement
            #    amount by this coin's value
            # 2) skip this coin and test the next coin, leaving amount unchanged
            return search(index, amount-coins[index]) + search(index+1, amount)

        # finally, return the output of our search function
        # starting at index 0 and the given amount
        return search(0, amount)
