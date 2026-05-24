from typing import List


'''
https://leetcode.com/problems/coin-change-ii/description/
'''
class Solution:
    # we will use a bottom up dynamic programming approach
    def change(self, amount: int, coins: List[int]) -> int:
        # first we will init our dynamic programming array
        # that will hold all the possible combinations of coins
        # for each amount up to amount
        # index -> amount of money, from 0 to amount
        # value -> the total number of combinations of coins
        #          to reach the index amount
        combinations = [0]*(amount+1)
        # our base case is that there is only 1 combination
        # that reaches an amount of $0: picking no coins
        combinations[0] = 1

        # loop through all coins first
        # if we swap looping through coins and our dp array
        # then we will get permutations, but we want combinations
        for coin in coins:
            # loop through our combinations dp array next
            # skiping the first index because that's our base case
            # remember the index i represents the amount of money
            # we are trying to make
            for i in range(1, len(combinations)):
                # calculate the difference between each amount i
                # and the coin we are trying to use
                difference = i - coin
                # for each difference that's larger than 0
                # we don't care if the difference is negative because
                # it means coin > amount i, so it's impossible to make
                # amount i using the coin
                if difference >= 0:
                    # increment the total number of combinations
                    # for this amount by the total number of combinations
                    # for the difference, because we can use that difference
                    # to make the amount with this coin
                    # remember, our base case is combinations[0] = 1
                    # so at the least we will be incrementing by 1 if
                    # our coin = amount i
                    combinations[i] += combinations[difference]

        # finallly, we will return the total number of combinations
        # for the final amount in the combinations array
        return combinations[amount]
