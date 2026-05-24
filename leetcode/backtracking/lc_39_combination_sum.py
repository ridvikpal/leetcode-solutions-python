from typing import List


'''
https://leetcode.com/problems/combination-sum/description/
'''
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # create our results list
        result = []
        # create our subset list
        subset = []
        # create our sum variable to store the total sum
        self.sum = 0

        # our recursive (depth first) search function to find
        # all combinations of candidates that sum to target
        def search(index):
            # our first base case is when sum = target
            # aka success
            if self.sum == target:
                # then add the subset to the result list
                result.append(subset.copy())
                # and return
                return

            # our second base case is when we are out of bounds
            # or when sum > target
            # aka failure
            if index >= len(candidates) or self.sum > target:
                # just immediately return
                return

            # first test with adding this candidate number
            subset.append(candidates[index])
            self.sum += candidates[index]
            
            # search on same index because we can choose
            # a candidate number an unlimited amount of times
            search(index)
            
            # second test without this number
            subset.pop()
            self.sum -= candidates[index]

            # search with next number, since we've already tried
            # including current number and excluding it
            search(index+1)

        # begin our search on index 0
        search(0)

        # return the result
        return result
