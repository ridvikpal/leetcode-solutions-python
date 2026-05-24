from typing import List


'''
https://leetcode.com/problems/search-in-rotated-sorted-array/description/
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # setup our standard left and right pointers
        # for binary search
        l = 0
        r = len(nums)-1

        # standard loop for binary search
        while l <= r:
            # get our middle index
            m = (l+r) // 2

            # check all our left, right and middle pointers
            # to see if we hit our target
            if nums[m] == target:
                return m
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r

            # if we haven't hit our target,
            # check if we are in left sorted range
            if nums[m] >= nums[l]:
                # if we are in left sorted range, then check
                # if target is in left sorted range
                if nums[l] < target < nums[m]:
                    # if target in left sorted range, search the left side
                    r = m - 1
                # else target is in right side, search the right side
                else:
                    l = m + 1
            # else we are in right sorted range
            else:
                # if we are in right sorted range, then check
                # if target is in right sorted range
                if nums[m] < target < nums[r]:
                    # if target is in right sorted range, search the right side
                    l = m + 1
                # else target is in left side, search the left side
                else:
                    r = m - 1

        # finally, if we don't find our target, return -1
        return -1
