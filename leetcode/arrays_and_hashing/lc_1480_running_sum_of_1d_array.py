from typing import List


'''
https://leetcode.com/problems/running-sum-of-1d-array/description/
'''
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # create a sum variable to
        # hold the running sum
        sum = 0

        # loop through all indexes
        # in the nums array
        for i in range(len(nums)):
            # increment the sum with the
            # current number in the array
            sum += nums[i]
            # replace that number in the array
            # with the running sum
            nums[i] = sum

        # finally, return the nums array
        return nums
