import math
from typing import List


'''
https://leetcode.com/problems/koko-eating-bananas/description/
'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # first we can handle the edge case
        # where we are given just 1 pile to consume
        if len(piles) == 1:
            # we can quickly calculate the optimal k
            # and return it because k = pile / time
            # which is opposite of time = pile / k
            # instead of math.ceil() you can also use
            # (pile + h-1) / h to round up for positive ints
            return math.ceil(piles[0] / h)

        # we can init the minimum k value as
        # being the maximum num of bananas in the pile
        # we know that for sure this will allow
        # koko to eat all the bananas the fastest
        min_k = max(piles)

        # we can setup a binary search to search
        # through all possible values of k to find
        # the optimal value
        # we essentially search for k from
        # [1, 2, 3, ..., max(piles)]
        # init our left and right pointers
        # from [0, ..., max(piles)-1] because
        # arrays are 0 indexed
        left = 0
        right = max(piles)-1

        # standard binary search loop
        # as long as left <= right
        while left <= right:
            # get the middle index
            middle = (left+right) // 2
            # get the k value at the middle index
            k = middle+1

            # we can calculate the total time
            # for eating all piles at this k value
            # init the time
            time = 0
            # loop through all piles
            for pile in piles:
                # increment the time it takes to 
                # eat each pile
                # instead of math.ceil() you can also use
                # (pile + k-1) / k to round up for positive ints
                time += math.ceil(pile / k)

            # if the time is greater than h,
            # our k value is too small and so
            # we are eating too slow
            if time > h:
                # we need to increase our k value
                # so search the right side of the array
                # and move left pointer to the right
                left = middle + 1
            # else our time is less than or equal to h
            # our k value is too fast or just right
            else:
                # anyhow update the min_k value 
                # to this k value
                # no need for min() function here
                # because we are guaranteed every time
                # we reach this line that k < min_k
                # thanks to binary search
                min_k = k
                # and decrease the k value for next iteration
                # to test eating slower
                # by moving right pointer to the left
                right = middle - 1

        # at the very end, we can return the minimum k we found
        return min_k
