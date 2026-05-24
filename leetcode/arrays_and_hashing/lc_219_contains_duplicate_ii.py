from typing import List


'''
https://leetcode.com/problems/contains-duplicate-ii/description/
'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # handle the edge case 
        # where if k = 0 it's impossible
        # find two duplicate numbers
        # with indices where abs(i-j) <= 0
        if k == 0:
            # so return false
            return False

        # we will use a dict that
        # maps a number to it's index
        # for each number we see as we
        # iterate through the nums list
        seen = dict()

        # loop through all indices in nums
        for i in range(len(nums)):
            # if the number at this index is
            # in our dict, we found a duplicate
            if nums[i] in seen:
                # then get the index for the duplicate number
                j = seen[nums[i]]
                
                # check if abs(i-j) <= k
                if abs(i - j) <= k:
                    # if so, we can return True
                    return True

            # otherwise add this number and
            # it's index to our seen dict
            seen[nums[i]] = i

        # if we make it to this point, we have
        # not found a duplicate number matching our
        # condition abs(i-j) <= k, so return false
        return False
