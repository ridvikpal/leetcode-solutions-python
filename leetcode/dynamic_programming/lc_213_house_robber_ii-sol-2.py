from typing import List


'''
https://leetcode.com/problems/house-robber-ii/description/
'''
class Solution:
    # we will use a top-down dynamic programming approach
    # where we memoize the result of a recursive search function
    def rob(self, nums: List[int]) -> int:
        # handle an edge case where we only have up to 2 houses
        if len(nums) <= 2:
            # in this case, simply rob the house with the most money
            return max(nums)

        # init our 2d memoization dict
        memoization = dict()

        # our recursive (backtracking) search function
        # that searches for the maximum money we can rob for
        # a specific number of houses (index of nums)
        def search(index, end_index):
            # our base case is if we are out of bounds
            # past the ending index we passed in
            if index > end_index:
                # simply return 0 in this case, since we can't
                # rob more money
                return 0

            # if we don't have a memoized value stored for this
            # particular search function call, then calculate
            # the max money at this index
            if (index, end_index) not in memoization:
                # at each iteration, we have two options
                # the first is that we rob the current house
                # and then skip to the house 2 steps over
                rob_house = nums[index] + search(index+2, end_index)
                # the second option is we skip robbing this house
                # and can rob the house 1 step over
                skip_house = search(index+1, end_index)

                # finally, we return the maximum money we got from both decisions
                memoization[(index, end_index)] = max(rob_house, skip_house)

            # finally, return the memoized value
            return memoization[(index, end_index)]

        # this problem is the exact same as the other house robber problem
        # but we can't simultaneously rob the first and last house
        # so we can simply test both cases
        # the first, we rob the first house and exclude the last house in our search
        # the second, we rob the last house and exclude the first house in our search
        return max(search(0, len(nums)-2), search(1, len(nums)-1))
