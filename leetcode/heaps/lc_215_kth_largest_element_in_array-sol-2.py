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

        # then we can use the nlargest method
        # to create an array of k largest numbers
        # and return the last one
        return heapq.nlargest(k, nums)[-1]
