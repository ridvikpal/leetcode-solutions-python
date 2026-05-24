from functools import cache
from typing import List


'''
https://leetcode.com/problems/house-robber/description/
'''
class Solution:
    # we will use a recursive top-down dynamic programming approach
    # to memoize a recursive function to solve this problem
    def rob(self, nums: List[int]) -> int:
        # create our recursive (backtracking) search function
        # that will search the maximum money we can rob at
        # a specific number of houses (index of nums)
        # we will use a @cache to automatically memoize the function
        @cache
        def search(index):
            # our base case is if we are out of bounds of the nums array
            if index >= len(nums):
                # in this case, there is no more money we can rob
                # so return 0
                return 0

            # at this index, we can make two decisions
            # first, we can first rob the current house at this index
            # and then rob the house 2 steps over
            rob_house = nums[index] + search(index+2)
            # or second, we can skip this house
            # which allows us to rob the next house
            skip_house = search(index+1)

            # we return the maximum value of both decisions
            return max(rob_house, skip_house)

        # begin our search at the first house (index = 0)
        # and return the maximum money we can rob
        return search(0)
