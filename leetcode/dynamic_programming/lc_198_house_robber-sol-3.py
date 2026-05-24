from typing import List


'''
https://leetcode.com/problems/house-robber/description/
'''
class Solution:
    # we will use a recursive top-down dynamic programming approach
    # to memoize a recursive function to solve this problem
    def rob(self, nums: List[int]) -> int:
        # init our memoization array
        memoization = [-1]*len(nums)

        # create our recursive (backtracking) search function
        # that will search the maximum money we can rob at
        # a specific number of houses (index of nums)
        def search(index):
            # our base case is if we are out of bounds of the nums array
            if index >= len(nums):
                # in this case, there is no more money we can rob
                # so return 0
                return 0

            # if we don't have any memoized value stored
            # then compute the max money at this index
            if memoization[index] == -1:
                # at this index, we can make two decisions
                # first, we can first rob the current house at this index
                # and then rob the house 2 steps over
                rob_house = nums[index] + search(index+2)
                # or second, we can skip this house
                # which allows us to rob the next house
                skip_house = search(index+1)

                # we memoize the maximum value of both decisions
                memoization[index] = max(rob_house, skip_house)

            # finally return our memoized value
            return memoization[index]

        # begin our search at the first house (index = 0)
        # and return the maximum money we can rob
        return search(0)
