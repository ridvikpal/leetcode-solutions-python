from typing import List


'''
https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
'''
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # we will utilize a reverse sorted array nums
        self.nums = sorted(nums, reverse=True)

        # store the k value we want to return
        self.k = k

    def add(self, val: int) -> int:
        # first we find the index to insert the value
        # into the sorted array to keep the array sorted
        # intialize the starting search index at 0
        i = 0
        # loop until we are out of bounds or
        # until we find a number in the array <= val
        while i < len(self.nums) and self.nums[i] > val:
            i += 1

        # insert the element at the correct index
        self.nums.insert(i, val)

        # return the kth largest element in the sorted nums array
        # we need to decrement by 1 because arrays are 0-indexed
        return self.nums[self.k-1]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
