from typing import List


'''
https://leetcode.com/problems/trapping-rain-water/description/
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        # init our total area that we will return
        total_area = 0

        # first we will calculate the maxmimum left heights
        # for all the indices, so init our max_left_height array
        max_left_height = [0] * len(height)
        # our base case is that our leftmost max left height
        # is just equal to the leftmost height
        max_left_height[0] = height[0]

        # loop through all height indices starting at 1
        for i in range(1, len(height)):
            # set the max left height to be the 
            # previous max left height or height at
            # the index just before i
            max_left_height[i] = max(max_left_height[i-1], height[i-1])

        # next we will calculate the maxmimum right heights
        # for all the indices, so init our max_right_height array
        max_right_height = [0]*len(height)
        # our base case is that our rightmost max right height
        # is just equal to the rightmost height
        max_right_height[-1] = height[-1]

        # loop through all height indices in reverse from
        # the second last last index
        for i in range(len(height)-2, -1, -1):
            # set the max right height to be the
            # previous max right height or height at
            # the index just after i
            max_right_height[i] = max(max_right_height[i+1], height[i+1])

        # now we can loop through all indices
        # from 1 to second last
        # we don't care about first or last index
        # because water cannot be trapped there
        for i in range(1, len(height)-1):
            # the area at this index is equal to the
            # minimum max height we found - the current height
            # at this index
            area = min(max_left_height[i], max_right_height[i]) - height[i]

            # the area may be negative, so we only
            # add to the total area if it's positive
            if area > 0:
                # add the positive area to the
                # total area
                total_area += area
        
        # finally, we will return the total area
        return total_area
