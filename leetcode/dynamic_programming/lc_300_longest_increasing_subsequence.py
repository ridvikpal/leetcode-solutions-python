from typing import List


'''
https://leetcode.com/problems/longest-increasing-subsequence/description/
'''
class Solution:
    # we will use a bottom up tabular dynamic programming
    # approach to solve this problem
    def lengthOfLIS(self, nums: List[int]) -> int:
        # first we will init our dynamic programming
        # memoization array that will hold the 
        # longest increasing subsequence (lis) length for
        # a particular index in nums
        # index -> maps to index in nums
        # value -> longest increasing subsequence up to index
        # we init all values to 1 because at the minimum
        # each index can hold a lis of 1 number
        lisArray = [1]*len(nums)
        
        # loop through all indices in nums
        for i in range(1, len(nums)):
            # loop through all indices in nums up to i
            # basically we will loop through 
            # all numbers to the left of i
            for j in range(i):
                # we will compare each number at j
                # to the base number at index i
                # if nums[j] < nums[i] then we have
                # an increasing subsequence if we include nums[i]
                if nums[j] < nums[i]:
                    # so we can include nums[i] to increase
                    # the lis by 1 up to index i assuming
                    # the last number in the lis is at index j
                    # so update our lisArray to be the max between
                    # 1 + lisArray[j] (because our lis is up to nums[j] + nums[i])
                    # or whatever was originally stored at lisArray[i]
                    lisArray[i] = max(1+lisArray[j], lisArray[i])


        # finally return the max lis we found at any index
        # it is not guarenteed in this problem that
        # the lis will be up to the end of the nums array
        return max(lisArray)
