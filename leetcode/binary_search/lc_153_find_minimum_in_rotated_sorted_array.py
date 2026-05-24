from typing import List


'''
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # init our final result
        result = float('inf')

        # setup our left and right pointers for binary search
        l = 0
        r = len(nums)-1

        # standard binary search loop as long as l <= r
        while l <= r:
            # first check if we are in a sorted range
            # if we are in sorted range, the smallest element
            # is the left value nums[l]
            if nums[l] < nums[r]:
                result = min(nums[l], result)

            # then check the middle value
            m = (l+r) // 2
            # check if the middle value is a minimum
            result = min(nums[m], result)

            # remember rotation creates two sorted ranges left and right
            # if we are in left sorted range, we need to search
            # the right sorted range
            if nums[m] >= nums[l]:
                # move left pointer to m + 1
                # to search right sorted range
                l = m + 1
            # else we are in right sorted range already
            # so search the left sorted range
            else:
                # move right pointer to m - 1
                # to search the left sorted range
                r = m - 1

        # return the result.
        return result
