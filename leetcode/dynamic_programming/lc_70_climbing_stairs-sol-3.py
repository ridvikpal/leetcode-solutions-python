'''
https://leetcode.com/problems/climbing-stairs/description/
'''
class Solution:
    # we can use a top-down dynamic programming approach
    # to memoize a recursive function to solve this problem
    def climbStairs(self, n: int) -> int:
        # we will init our memoization array
        # where index -> height of stairs - 1
        # value -> # of total combinations to reach
        #          this height of stairs
        # note that arrays are 0-indexed so index+1
        # equals the actual height of stairs
        memoization = [-1]*n

        # create our recursive (backtracking) search function
        # that will search the number of ways
        # we can reach a specific height of stairs
        # in descending fashion
        def search(height):
            # our first base case is when
            # we reach a height of 0
            if height == 0:
                # in this case, we have found a valid
                # combination, so return 1
                return 1

            # our second base case is when
            # we reach a negative height
            if height < 0:
                # in this case ,we have found an invalid
                # combination, so return 0
                return 0

            # first check if we have already memoized
            # the result of our search function for
            # height-1. We have to do -1 because
            # arrays are 0-indexed
            if memoization[height-1] > -1:
                # if so, then return the value
                return memoization[height-1]
            
            # finally we will recursively search
            # through our 2 decisions, sum the result
            # and store it in our memoization array
            # 1) to get to this height, we took 1 step
            #    so recurse backwards 1 step
            # 2) to get to this height, we took 2 steps
            #    so recurse backwards 2 steps
            memoization[height-1] = search(height-1) + search(height-2)

            # finally just return the memoization array value
            return memoization[height-1]
        
        # we will begin our search assuming
        # we are at a height n
        return search(n)
