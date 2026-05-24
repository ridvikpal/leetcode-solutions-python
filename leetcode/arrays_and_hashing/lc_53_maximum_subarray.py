import math
from typing import List


'''
https://leetcode.com/problems/maximum-subarray/description/
'''
class Solution:
    # We will use Kadane's algorithm to solve this problem
    def maxSubArray(self, nums: List[int]) -> int:
        # init our initial max sum
        # to negative infinity
        max_sum = -math.inf

        # init our current sum
        # which will update as we
        # iterate through the nums array
        current_sum = 0
        
        # loop through all numbers in the nums array
        for num in nums:
            # increment the current sum with this num
            # essentially extending our subarray to include
            # this number
            current_sum += num
            
            # update the max sum if our
            # current sum is larger
            max_sum = max(current_sum, max_sum)
            
            # if our current sum is negative
            # then there is no point in adding
            # more numbers to this subarray
            if current_sum < 0:
                # reset our current sum
                # essentially resetting our subarray
                # to an empty set, so we can start
                # a new subarray on the next iteration
                # with the next number
                current_sum = 0

        # finally, return the max sum we found
        return max_sum
