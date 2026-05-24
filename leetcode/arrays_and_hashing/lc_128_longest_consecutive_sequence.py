from typing import List


'''
https://leetcode.com/problems/longest-consecutive-sequence/description/
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # first handle the edge case where
        # we have an empty nums array
        if not nums:
            return 0
        
        # first create a set to remove duplicates
        unique_nums = set(nums)

        # initialize the max consecutive sequence length
        max_sequence_length = 1
        
        for num in unique_nums:
            # first check if any number less
            # than this number exists in our set
            # if it does not, then we have the start 
            # of a consecutive sequence
            if num-1 not in unique_nums:
                # initialize our temporary sequence length
                sequence_length = 1

                # we have start of a sequence
                # so we can check how many consecutive
                # numbers are in our sequence by looping
                # as long as there are consecutive numbers
                # in our set
                while num+1 in unique_nums:
                    # update the sequence length
                    sequence_length += 1
                    # increment the last number
                    # in our consecutive sequence
                    num += 1

                # update the max consecutive sequence length
                max_sequence_length = max(sequence_length, max_sequence_length)

        # finally return the max conseuctive sequence length
        return max_sequence_length
