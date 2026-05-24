from typing import List


'''
https://neetcode.io/problems/trapping-rain-water/question
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        # init our total area to 0
        total_area = 0

        # loop through all indices from 1 to 2nd last
        # we don't care about the heights for the first
        # and last indexes because it's impossible for
        # water to get trapped there
        for i in range(1, len(height)-1):
            # init our max left height
            max_left_height = 0
            # init our max right height
            max_right_height = 0

            # init our left pointer to the
            # element before index i
            left = i-1
            # init our right pointer to the
            # element after index i
            right = i+1

            # loop as long as left pointer is within bounds
            # to find the max height to the left of index i
            while left >= 0:
                # update the max left height
                max_left_height = max(max_left_height, height[left])
                # decrement the left pointer
                left -= 1

            # loop as long as the right pointer is within bounds
            # to find the max height to the right of index i
            while right < len(height):
                # update the max right height
                max_right_height = max(max_right_height, height[right])
                # increment the left pointer
                right += 1

            # finally, the max area of water that can be stored at index i
            # is equal to the height at index i subtracted from the 
            # minimum of the left/right heights we found
            max_area = min(max_left_height, max_right_height) - height[i]
            
            # then update the total area with our max area
            # as long as it is non-negative
            if max_area > 0:
                total_area += max_area

        # finally, return the total area we found 
        return total_area
