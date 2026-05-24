from functools import cache
from typing import List


'''
https://leetcode.com/problems/min-cost-climbing-stairs/description/
'''
class Solution:
    # we will use a top-down dynamic programming approach
    # by memoizing a recursive function to solve this problem
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # create our recursive (backtracking) search function
        # which will search all possible combinations to get
        # the minimum cost to climb the stairs
        # we will use @cache for automatic memoization
        @cache
        def search(index):
            # our base case is when we are
            # out of bounds of the index
            if index >= len(cost):
                # in this case, we can simply return 0
                # because there are no more costs to add
                # since we have reached the top of the staircase
                return 0

            # we can recurse on both decisions to climb the stairs
            # 1) take this stair and then decide on the next step
            # 2) take this stair and then decide on the second next step
            choose_one_step = cost[index] + search(index+1)
            choose_two_steps = cost[index] + search(index+2)

            # and finally, we will choose the minimum cost from
            # both decision and return that value
            return min(choose_one_step, choose_two_steps)

        # since we have the option of beginning from index 0
        # or index 1, we can try both options and return
        # the minimum cost we find
        return min(search(0),search(1))
