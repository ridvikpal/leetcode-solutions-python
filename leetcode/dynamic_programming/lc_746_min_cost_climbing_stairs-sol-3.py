from typing import List


'''
https://leetcode.com/problems/min-cost-climbing-stairs/description/
'''
class Solution:
    # we will use a top-down dynamic programming approach
    # by memoizing a recursive function to solve this problem
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # init our memoization array
        # index -> each step, same as index in cost array
        # value -> the minimum cost of climbing stairs
        #          for that step
        memoization = [-1]*len(cost)

        # create our recursive (backtracking) search function
        # which will search all possible combinations to get
        # the minimum cost to climb the stairs
        def search(index):
            # our base case is when we are
            # out of bounds of the index
            if index >= len(cost):
                # in this case, we can simply return 0
                # because there are no more costs to add
                # since we have reached the top of the staircase
                return 0

            # first check if we have a memoized value stored
            # for this function call
            if memoization[index] > -1:
                return memoization[index]

            # we can recurse on both decisions to climb the stairs
            # 1) take this stair and then decide on the next step
            # 2) take this stair and then decide on the second next step
            choose_one_step = cost[index] + search(index+1)
            choose_two_steps = cost[index] + search(index+2)

            # we will choose the minimum cost from
            # both decision and update our memoized array
            memoization[index] = min(choose_one_step, choose_two_steps)

            # finally return the memoization value we stored
            return memoization[index]

        # since we have the option of beginning from index 0
        # or index 1, we can try both options and return
        # the minimum cost we find
        return min(search(0),search(1))
