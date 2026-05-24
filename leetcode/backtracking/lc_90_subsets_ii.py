from typing import List


'''
https://leetcode.com/problems/subsets-ii/description/
'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # first sort our nums array because it can contain duplicates
        # this puts duplicates right next to one another
        nums.sort()
        
        # create our results array
        # this will contain subsets
        result = []
        # create our subset array
        subset = []
        
        # our recursive search function to search through all possible subsets
        def search(index):
            # our base case is when we have looped through all possible indices
            # and are out of bounds
            if index >= len(nums):
                # then we have a valid subset
                # so we can add a copy of the subset
                # to the results array
                result.append(subset.copy())
                # and return
                return

            # first test with ADDING our number to the subset
            subset.append(nums[index])
            # then recursively call search with next index
            search(index+1)
            
            # second test with REMOVING our number from the subset
            subset.pop()
            # We want to make sure we don't add a duplicate number again
            # to the subset and so increment until we no longer see a duplicate
            while (index < len(nums)-1 and nums[index] == nums[index+1]):
                index += 1
            # then recursively call search with next index
            search(index+1)

        # begin the search with the starting index 0
        search(0)

        # return the result.
        return result
