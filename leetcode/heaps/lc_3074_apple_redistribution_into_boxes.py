import heapq
from typing import List


'''
https://leetcode.com/problems/apple-redistribution-into-boxes/description/
'''
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        # first we can calculate the total
        # number of apples we have to redistribute
        total_apples = sum(apple)

        # then we can create a capacity array
        # where all the values are inverted
        # because we need to create a max heap
        # and python3 < version 3.14 only supports min heap
        negative_capacity = [-cap for cap in capacity]

        # we will heapify our negative capacity array
        # to create a max heap
        heapq.heapify(negative_capacity)

        # init the count of boxes we will use for redistribution
        count = 0

        # loop as long as there is capacity to use
        # and as long as there are apples to redistribute
        while negative_capacity and total_apples > 0:
            # we always want to use the max capacity first
            # so pop it from the heap
            max_capacity = -heapq.heappop(negative_capacity)
            # then subtract it from the number of total apples
            # effectively place apples in that capacity box
            total_apples -= max_capacity
            # increment the count because we used 1 more box
            count += 1

        # finally return the count of boxes we
        # used for redistribution
        return count
