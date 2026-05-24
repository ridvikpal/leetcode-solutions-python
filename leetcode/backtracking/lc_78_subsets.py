from typing import List


'''
https://leetcode.com/problems/subsets/description/
'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # init our results array
        # which will contain all subsets
        result = []

        # setup our subset array
        # this will hold a possible subset
        # to add to our result array
        subset = []

        # our backtracking (recursive)
        # search function to search all possible
        # combinations of a set
        # on each iteration we will test 2 options
        # 1) add the number at index
        # 2) don't add the number at index (skip it)
        def search(index):
            # our base case is if we
            # are out of bounds of iteration
            if index >= len(nums):
                # if we are out out bounds, then
                # we have a possible subset
                # so add it to the reuslts array
                result.append(subset.copy())
                # and return
                return
            
            # first test with ADDING the number
            # to the subset
            subset.append(nums[index])
            # and go to the next number in nums
            search(index+1)
            
            # after backtracking
            # test with SKIPPING the number
            # (not adding it)
            subset.pop()
            # and go to the next number in nums
            search(index+1)

        # begin our search at index 0
        search(0)

        # finally return the result array
        return result
