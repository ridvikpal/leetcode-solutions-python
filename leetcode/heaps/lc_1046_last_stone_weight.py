import heapq
from typing import List


'''
https://leetcode.com/problems/last-stone-weight/description/
'''
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # first negate all stone values
        # because we will be using python's min heap
        # but we actually want a max heap
        negative_stones = [-stone for stone in stones]
        # heapify using heapq to create a negative min heap
        # (aka. max heap)
        heapq.heapify(negative_stones)

        # loop until we have 1 stone or less left
        while len(negative_stones) >= 2:
            # get the two heaviest stones in the heap
            # we have to negate output of each heappop()
            # because we are using negative min heap
            first_stone = -heapq.heappop(negative_stones)
            second_stone = -heapq.heappop(negative_stones)

            # smash the two stones together, and calculate
            # the absolute value of the result
            smash_result = abs(first_stone - second_stone)

            # check if the two stones didn't destroy each other
            # which is when smash result != 0
            if smash_result != 0:
                # then add the smash result, which is the resultant stone
                # back into the heap after negating it
                heapq.heappush(negative_stones, -smash_result)

        # finally, if we have 1 stone left, return it
        if len(negative_stones) == 1:
            return -negative_stones[0]

        # otherwise return 0
        return 0
            