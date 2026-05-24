from typing import List


'''
https://leetcode.com/problems/permutations/description/
'''
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # create our results array
        result = []

        # our recursive search function
        # it will search all possible permutations 1 by 1
        def search(start_index):
            # our base case is when our start_index is out of bounds
            # or last value
            if start_index >= len(nums)-1:
                # in this case, add our current number order
                # to the results array and return
                result.append(nums.copy())
                return

            # loop through all indexes in the array from start_index to end index
            for i in range(start_index, len(nums)):
                # for each number at index i, swap it with number 
                # at start_index
                nums[start_index], nums[i] = nums[i], nums[start_index]
                
                # now continue searching at the next start index
                # this fixes our current swapped element and moves onto
                # the next one.
                search(start_index+1)

                # now reset the above swap after backtracking so the array
                # can loop again
                nums[start_index], nums[i] = nums[i], nums[start_index]
            
        # begin our search for permutations at start_index = 0
        search(0)

        # return the result array
        return result
