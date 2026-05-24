from typing import List


'''
https://leetcode.com/problems/combination-sum-ii/description/
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # first sort the candidates array
        # sorting will place the duplicates right next to one another
        candidates.sort()
        
        # keep our results array
        result = []
        # keep our total sum
        self.sum = 0
        # keep our subset array
        subset = []

        # our recursive search function (really a dfs)
        # that searches through all possible subsets of numbers
        def search(index):
            # our first base case is when the sum = target
            if self.sum == target:
                # in this case, add the subset to our results array and return
                result.append(subset.copy())
                return

            # our second base case is when the sum > target
            # or we are indexed out of bounds
            if self.sum > target or index >= len(candidates):
                # int his case, simply return, no point exploring further
                # since we have only positive numbers, ensuring the sum only increases
                return

            #--- First test WITH including the number in our subset ---
            # add the number to our subset
            subset.append(candidates[index])
            # Increment our total sum
            self.sum += candidates[index]
            # go to the next number in our candidates array
            search(index+1)

            # --- Now test WITHOUT including the number in our subset AFTER BACKTRACKING ---
            # Remove number from our subset
            subset.pop()
            # Decrement our tota l sum
            self.sum -= candidates[index]
            
            # to ensure we don't just add the same (duplicate) number to
            # our subset again, loop until the next number is not the same as
            # the current number or we are out of bounds
            while index < len(candidates)-1 and candidates[index] == candidates[index+1]:
                index += 1

            # go to the next number in our candidates array
            search(index+1)


        # we will begin our search at 0
        search(0)

        # return our results array
        return result
