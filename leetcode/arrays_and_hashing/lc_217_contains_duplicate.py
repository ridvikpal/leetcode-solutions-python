from typing import List


'''
https://leetcode.com/problems/contains-duplicate/description/
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # first create a set to store nums we have seen before
        seen = set()

        # loop through all numbers
        for num in nums:
            # if we have seen this number before
            # then return true because it is a duplicate
            if num in seen:
                return True

            # else we have not seen this number before
            # so add it to the seen set
            seen.add(num)

        # if we loop through all numbers and
        # don't find any duplicates, return False
        return False
