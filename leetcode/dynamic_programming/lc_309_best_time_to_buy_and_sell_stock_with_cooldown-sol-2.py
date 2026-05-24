from typing import List


'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
'''
class Solution:
    # we will use a top down dynamic programming approach
    # to memoize a recursive function
    def maxProfit(self, prices: List[int]) -> int:
        # init our memoization dict
        # we need a dict because our keys
        # will be (index, state) tuples
        # rather than just indices
        memoization = dict()

        # init our recursive (backtracking) search function that will
        # search through all possibilities to find the optimal profit
        # the index is the index of the price array we are considering
        # and the state is either 'buy', 'sell', or 'cooldown'
        def search(index, state):
            # our base case for recrusion is
            # if our index is out of bounds
            if index >= len(prices):
                # in this case, we can simply return 0
                # because there is no more money we can make
                # if we are out of index bounds on the price array
                return 0

            # always check if we already have this 
            # index and state in our memoization dict first
            if (index, state) in memoization:
                # if we do, we can simply return it
                return memoization[(index, state)]

            # our first state case is buying
            if state == 'buy':
                # our first option is to buy at this index
                # so we lose money to buy at this price
                # recurse to the next state which is selling
                # on the next index
                choose_buy = search(index+1, 'sell') - prices[index]
                
                # our second option is to skip buying this index
                # so simply recurse to the next index with
                # the same buy state
                choose_skip = search(index+1, 'buy')

                # update our memoization dict with the optimal
                # value for this index and state
                memoization[(index, 'buy')] = max(choose_buy, choose_skip)
            # our second state case is selling
            elif state == 'sell':
                # always check if we already have this 
                # index and state in our memoization dict first
                if (index, 'sell') in memoization:
                    # if we do, we can simply return it
                    return memoization[(index, 'sell')]

                # our first option is selling at this index
                # so we gain money by selling at this price
                # recurse to the next state which is cooldown
                # on the next index
                choose_sell = search(index+1, 'cooldown') + prices[index]

                # our second option is to skip selling at this index
                # so simply recurse to the next index with
                # the same sell state
                choose_skip = search(index+1, 'sell')

                # update our memoization dict with the optimal
                # value for this index and state
                memoization[(index, 'sell')] = max(choose_sell, choose_skip)
            # our final state case is cooldown
            elif state == 'cooldown':
                # we can't do anything here except 
                # recurse to the next index with the
                # next state which is the buy state
                # and update the memoization dict with the result
                memoization[(index, 'cooldown')] = search(index+1, 'buy')
            
            # return the memoization dict value we updated
            # in the if statements
            return memoization[(index, state)]

        # we will simply return the output of the search function
        # starting our search at index 0 with the 'buy' state
        return search(0, 'buy')
