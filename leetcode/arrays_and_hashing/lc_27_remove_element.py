from typing import List


'''
https://leetcode.com/problems/remove-element/description/
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # we can use list comprehension
        # to remove all nums that match val
        # and assign it to nums in place using slicing [:]
        nums[:] = [num for num in nums if num != val]

        # finally return the length of the numbers
        # array, now without the occurance of val
        return len(nums)
