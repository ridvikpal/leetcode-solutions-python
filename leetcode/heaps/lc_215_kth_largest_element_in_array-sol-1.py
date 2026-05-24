import heapq
from typing import List


'''
https://leetcode.com/problems/kth-largest-element-in-an-array/description/
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # first we create a min heap 
        # from the nums array
        heapq.heapify(nums)

        # we will remove the minimum elements
        # from the min heap until we have k nums
        # in our min heap
        while len(nums) > k:
            heapq.heappop(nums)

        # now, we will be left with a heap
        # that contains the k largest nums
        # so we can return the smallest of these
        # k largest nums
        return nums[0]
