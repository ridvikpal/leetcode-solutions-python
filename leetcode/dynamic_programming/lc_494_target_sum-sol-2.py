from typing import List


'''
https://leetcode.com/problems/target-sum/description/
'''
class Solution:
    # we can use a top-down dynamic programming approach
    # where we memoize the result of a recursive function
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # init our memoization dict
        # we need a dict because our key
        # will be a tuple (index, target)
        memoization = dict()

        # create our recursive (backtracking) function
        # to search all possible combinatons of nums
        # that equals target
        def search(index, target):
            # our base case is when we are
            # out of bounds in our index
            if index >= len(nums):
                # check if the target is 0
                # this means we have found a valid
                # combination
                if target == 0:
                    # we can return 1 because we found
                    # 1 combination
                    return 1
                # else the target is non-zero
                # this means we have not found 
                # a valid combination
                else:
                    # we can return 0 because we have
                    # found 0 combinations
                    return 0

            # first check if we have a memoized value stored
            if (index, target) in memoization:
                # if we do, simply return it
                return memoization[(index, target)]

            # now we can recursively search on our 2 decisions:
            # 1) we add this number in nums
            # 2) we subtract this number in nums
            # and then add it to our memoization array
            memoization[(index, target)] = search(index+1, target-nums[index]) + search(index+1, target+nums[index])

            # and then return the memoization value we just stored
            return memoization[(index, target)]

        # we will begin searching at index 0 and trying to find target
        return search(0, target)
