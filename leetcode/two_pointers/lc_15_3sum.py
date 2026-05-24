from typing import List


'''
https://leetcode.com/problems/3sum/description/
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # first we will sort the array
        # to place duplicates next to one another
        nums.sort()

        # init our result array
        result = []

        # loop through all indices in nums
        for i in range(len(nums)):
            # if we find any duplicate numbers
            # after the first number at i = 0
            if i > 0 and nums[i-1] == nums[i]:
                # then skip it so continue
                continue

            # setup our two pointer approach
            # left pointer points to number after i
            left = i+1
            # right pointer points to last number in array
            right = len(nums)-1

            # loop as long as the left/right pointers don't overlap
            while left < right:
                # compute the three_sum
                three_sum = nums[i] + nums[left] + nums[right]

                # if our three sum = 0 then we have a valid combo
                if three_sum == 0:
                    # add this combo to our results array
                    result.append([nums[i], nums[left], nums[right]])

                    # now we want to try out another combination, so
                    # increment our left pointer
                    left += 1
                    # decrement our right pointer
                    right -= 1

                    # skip duplicates on the left pointer
                    # we don't need to skip duplicates on right pointer
                    # since out of our 3 numbers, as long as 2 out of 3
                    # are unique, we are ok and will never had duplicate entries
                    while left < right and nums[left-1] == nums[left]:
                        # increment our left pointer until we don't have duplicates
                        left += 1

                # else if our three sum is less than 0
                elif three_sum < 0:
                    # then increment the left pointer
                    # to increase the three sum
                    left += 1
                # else our three sum is greater than 0
                else:
                    # the decrement the right pointer
                    # to decrease the three sum
                    right -= 1

        # finally, return the results array
        return result
