from typing import List


'''
https://leetcode.com/problems/min-cost-climbing-stairs/description/
'''
class Solution:
    # we will use dynamic programming with a bottom up
    # tabular memoization method
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # our base case  is if we are climbing 2 steps
        if len(cost) == 2:
            # we will always choose the stair with the least cost
            # because we can always get to the top floor
            # from either step directly
            # from index 0 -> take 2 steps get to top floor (index 2)
            # from index 1 -> take 1 step get to top floor (index 2)
            return min(cost[0], cost[1])
        
        # otherwise, we can setup a minCost array
        # that will track the minimum cost to get to
        # floor at the array index
        # because we want to reach floor at index
        # greater than max index of cost array
        # our minCost array will be 1 larger in length
        # than the given cost array
        # the final index will hold the final cost to get
        # to the top floor
        # all indices will be initialized with cost of 0 to begin
        minCost = [0]*(len(cost)+1)

        # loop through all indices from 2 to final index in minCost array
        # the first two indices (0 and 1) technically have no cost to get to
        # since we get to pick where to begin for free
        for i in range(2, len(minCost)):
            # the minCost for each index of the staircase
            # is always equal to minimum of
            # 1) the previous minCost + stair cost for last index
            # 2) the previous minCost + stair cost for second last index
            minCost[i] = min(minCost[i-1]+cost[i-1], minCost[i-2]+cost[i-2])

        # finally, return the minCost to reach the top floor
        # which is the last index in the minCost array
        return minCost[len(cost)]
