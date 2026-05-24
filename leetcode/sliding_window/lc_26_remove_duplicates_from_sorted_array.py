from typing import List


'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # handle edge case where we are given
        # a list with only 1 element
        # then no need to remove duplicates
        if len(nums) == 1:
            return 1

        # we will use a 2 pointer approach
        # first pointer i initially
        # points to the last element
        i = len(nums)-1
        # second pointer j always points
        # to the element in front of 
        # the first pointer
        j = i-1

        # loop until the j is out of bounds
        while j >= 0:
            # if the two pointers point
            # to the same number
            # then remove the rightmost number
            if nums[i] == nums[j]:
                del nums[i]

            # decrement both pointers
            # moving right to left
            i -=1
            j -=1
        
        # finally return the length of nums
        # after removing all duplicates       
        return len(nums)
