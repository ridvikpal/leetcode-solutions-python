from typing import List


'''
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
'''
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # we can use a binary search method
        # because the input array is sorted
        # init our left pointer to point
        # to the leftmost element
        left = 0
        # init our right pointer to point
        # to the rightmost element
        right = len(numbers)-1

        # loop as long as the left element
        # is smaller than the right element
        # we don't need <= because we can't
        # return the same indices
        while left < right:
            # compute the sum of left + right nums
            test_sum = numbers[left] + numbers[right]

            # check if the sum is our target
            if test_sum == target:
                # if it is, we can return
                # our 1-indexed indices
                return [left+1, right+1]

            # else check if the sum is less than the target
            # if it is, we need to make our sum bigger
            if test_sum < target:
                # so increment the left pointer
                left += 1
            # else the number is larger than the target
            # and we need to make our sum smaller
            else:
                # so decrement the right pointer
                right -= 1
