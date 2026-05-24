from typing import List


'''
https://leetcode.com/problems/partition-equal-subset-sum/description/
'''
class Solution:
    # we will use a dynamic programming bottom up approach
    # with a set instead of the usual array
    def canPartition(self, nums: List[int]) -> bool:
        # first get the total sum of the numbers
        total_sum = sum(nums)

        # if the total sum is odd
        # then there is no way to split it
        # into two equal ints
        if total_sum % 2 != 0:
            # so we can return false immediately
            return False

        # now init our memoization set
        # this will hold all possible subset sums
        # as we iterate through the numbers in the nums array
        sum_set = set()
        # our base case for the set is when we have
        # selected no numbers out of the nums array
        # this is a sum of 0, so add it to the set
        sum_set.add(0)

        # loop through all numbers in nums
        for num in nums:
            # our base case for looping is when
            # we have found half the total sum in the sum set
            if total_sum / 2 in sum_set:
                # if we find this during iteration, then logically
                # the rest of the numbers in the set
                # must sum to the other half and so
                # it is possible to partition the array
                # into two subsets of equal value
                # so we can return True
                return True

            # otherwise create a temporary set
            # hold all the new sums we will eventually
            # add to the sum_set
            temp_set = set()

            # loop through all previous sums we have in our sum set
            for previous_sum in sum_set:
                # add the current number to all of those previous values
                # and add the result to the temp set
                temp_set.add(previous_sum+num)
            # finally merge the temp set into the sum set
            # to add the new possible subset sums into the sum set
            sum_set.update(temp_set)

        # if we reach this point then we have iterated through
        # the entire array and not been able to make a sum of
        # total sum / 2 so return False
        return False
