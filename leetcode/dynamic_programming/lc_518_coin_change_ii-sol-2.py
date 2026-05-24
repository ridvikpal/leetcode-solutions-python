from typing import List


'''
https://leetcode.com/problems/coin-change-ii/description/
'''
class Solution:
    # we will use a top-down dynamic programming approach
    # by memoizing a recursive function to solve this problem
    def change(self, amount: int, coins: List[int]) -> int:
        # setup our memoization dict
        # we need a dict because our keys
        # will be (index, amount) tuples
        memoization = dict()

        # we can define our recursive (backtracking) search
        # function that searches through all possible combinations
        # of coins and keeps count of the ones that make up the amount
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
            
            # first check if we already have the result
            # for this index and amount stored in our
            # memoization dict
            if (index, amount) in memoization:
                # if we do, then return it's value directly
                return memoization[(index, amount)]
            
            # otherwise, update the memoization dict 
            # by using 2 decisions on each recursion step:
            # 1) use this coin at index specifically and decrement
            #    amount by this coin's value
            # 2) skip this coin and test the next coin, leaving amount unchanged
            memoization[(index, amount)] = search(index, amount-coins[index]) + search(index+1, amount)

            # finally, return the memoization dictionary value
            return memoization[(index, amount)]

        # finally, return the output of our search function
        # starting at index 0 and the given amount
        return search(0, amount)
