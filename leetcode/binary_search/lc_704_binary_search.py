from typing import List


'''
https://leetcode.com/problems/binary-search/description/
'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # we will use a standard binary search for this
        # start with our left pointer pointing to the
        # first element
        left = 0
        # and our right pointer pointing to the last element
        right = len(nums)-1

        # we loop as long as the left pointer is
        # before or equal to the right pointer
        while left <= right:
            # get the index of the middle between
            # the two left/right pointers
            # (aka. the pivot)
            # making sure to round down to 2
            middle = (left + right) // 2
            
            # check if the element at the middle
            # element equals the target value
            if nums[middle] == target:
                # if it does, return the middle index
                return middle

            # otherwise, check if the target is smaller
            # than the middle element
            if target < nums[middle]:
                # if it is, then the element is to the left
                # of the middle pivot
                # so we need to move our right pointer 
                # to middle - 1
                right = middle - 1
            # else the target is greater than the middle
            # element
            else:
                # so the element is to the right
                # of the middle pivot
                # so we need to move our left pointer
                # to middle + 1
                left = middle + 1

        # if we get to this point, we have searched
        # the whole array and not found the element
        # so return -1
        return -1
