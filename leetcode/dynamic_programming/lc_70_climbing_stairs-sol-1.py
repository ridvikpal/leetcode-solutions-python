'''
https://leetcode.com/problems/climbing-stairs/description/
'''
class Solution:
    # we will use a dynamic programming approach with
    # bottom up (tabular) memoization method
    # this is essentially a fibonacci sequence problem
    def climbStairs(self, n: int) -> int:
        # first we can setup our base case
        # if we are climbing less than 2 steps:
        # 1 step -> only 1 way, climb 1 step
        # 2 steps -> only 2 ways, climb 2 steps or 1+1 steps
        if n <= 2:
            # so we can return n directly
            return n

        # otherwise we can setup our memoized steps array
        # that will iteratively build up a solution
        # for how many steps are possible (bottom up)
        # we init all values with -1 at the beginning
        # remember that arrays are 0-indexed, so
        # index 0 -> possible combinations for 1 step
        # index 1 -> possible combinations for 2 steps
        # and so on
        steps = [-1]*n

        # init our base cases
        # 1 step -> only 1 way, climb 1 step
        steps[0] = 1
        # 2 steps -> only 2 ways, climb 2 steps or 1+1 steps
        steps[1] = 2

        # loop through all numbers until n-1
        for i in range(2, n):
            # the next number of steps on each iteration
            # is equal to the sum of the previous 2 steps
            # we have already calculated
            # because for each individual subproblem we can choose
            # to make 1 single step or 2 steps
            steps[i] = steps[i-1] + steps[i-2]

        # finally return the final steps array value, index n-1
        # because arrays are 0-indexed
        return steps[n-1]
