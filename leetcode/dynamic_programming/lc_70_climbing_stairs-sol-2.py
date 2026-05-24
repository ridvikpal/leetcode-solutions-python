from functools import cache


'''
https://leetcode.com/problems/climbing-stairs/description/
'''
class Solution:
    # we can use a top-down dynamic programming approach
    # to memoize a recursive function to solve this problem
    def climbStairs(self, n: int) -> int:
        # create our recursive (backtracking) search function
        # that will search the number of ways
        # we can reach a specific height of stairs
        # in descending fashion
        # we will use @cache to automatically
        # memoize the function outputs
        @cache
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
            
            # finally we will recursively search
            # through our 2 decisions, sum the result and return:
            # 1) to get to this height, we took 1 step
            #    so recurse backwards 1 step
            # 2) to get to this height, we took 2 steps
            #    so recurse backwards 2 steps
            return search(height-1) + search(height-2)
        
        # we will begin our search assuming
        # we are at a height n
        return search(n)
