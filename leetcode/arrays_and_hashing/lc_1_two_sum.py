from collections import defaultdict
from typing import List


'''
https://leetcode.com/problems/two-sum/description/
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a dictionary to map nums array
        # values to indexes
        numToIndex = defaultdict(int)

        # loop through all elements in nums array
        for i in range(len(nums)):
            # populate the numToIndex dictionary
            numToIndex[nums[i]] = i

        # loop through all elemnts in the nums array again
        for i in range(len(nums)):
            # calculate the difference we need to get
            difference = target - nums[i]
            # if we have the difference stored in our dictionary key
            # and the index of that difference is not the same as
            # our current index, then return current index + stored index
            if difference in numToIndex and numToIndex[difference] != i:
                return [i, numToIndex[difference]]
