import heapq
from typing import List


'''
https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
'''
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # first start off by storing k
        self.k = k

        # next we will use a min heap
        # to keep track of the kth largest number
        self.k_heap = nums
        heapq.heapify(nums)

        # the size of our min heap will be k elements
        # this is because then the minimum of
        # those k elements is the kth largest
        # which is the first element of the heap
        # so keep removing excess elements above k elements
        while len(self.k_heap) > self.k:
            heapq.heappop(self.k_heap)

    def add(self, val: int) -> int:
        # if we have less than k elements in our heap
        # then just add to the heap until we have k elements
        if len(self.k_heap) < self.k:
            heapq.heappush(self.k_heap, val)
        # else we already have k elements, so replace the
        # correct element in the heap with heappushpop()
        else:
            heapq.heappushpop(self.k_heap, val)

        # finally return the first element in the heap,
        # which is the k largest
        return self.k_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
