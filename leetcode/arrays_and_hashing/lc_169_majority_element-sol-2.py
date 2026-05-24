from typing import List


'''
https://leetcode.com/problems/majority-element/description/
'''
class Solution:
    # We can use the Boyer-Moore Majority Voting Algorithm
    # because we know a majority element is guaranteed
    # for O(1) space
    def majorityElement(self, nums: List[int]) -> int:
        # start by initializing a majority candidate
        candidate = 0
        # and initialize a count to keep track
        # of how often we see this candidate
        count = 0

        # loop through all numbers
        for num in nums:
            # if the count is 0
            if count == 0:
                # the candidate is set to
                # the current number
                candidate = num
                # and count set to 1 since
                # we just saw it
                count = 1
            # else if the current number = candidate
            elif num == candidate:
                # increment the count
                count += 1
            # else the current number != candidate
            else:
                # decrement the count
                # to ensure that eventually our
                # candidate is set to another number
                # when count = 0
                count -= 1

        # and the end we are guaranteed to have our
        # candidate equal the majority as long as 
        # there is a majority in our sequence
        return candidate
