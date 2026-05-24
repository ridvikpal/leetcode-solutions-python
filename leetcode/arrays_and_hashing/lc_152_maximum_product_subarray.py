import math
from typing import List


'''
https://leetcode.com/problems/maximum-product-subarray/description/
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # init our max product to -infinity
        max_product = -math.inf
        # init a flag used to keep track of
        # whether the nums array contains a 0
        contains_zero = False
        
        # init our current max product to 1
        current_product = 1

        # we will loop through all nums left to right
        # to find the maximum product in that direction
        for num in nums:
            # if the current number is 0
            # we will essentially skip it
            # because multiplying by 0 equals 0
            if num == 0:
                # reset the current product to 1
                # that way the next number on next
                # iteration will create a new subarray
                # to begin counting from
                current_product = 1
                # set the contains zero flag to True
                contains_zero = True
            # else the number is non-zero
            else:
                # multiply the current product
                # by current number and keep track of it
                current_product *= num
                # update the max product if required with
                # the current product
                max_product = max(current_product, max_product)


        # init our current max product to 1
        current_product = 1

        # then we will loop through all nums right to left
        # to find the maximum product in that direction
        for num in nums[::-1]:
            # if the current number is 0
            # we will essentially skip it
            # because multiplying by 0 equals 0
            if num == 0:
                # reset the current product to 1
                # that way the next number on next
                # iteration will create a new subarray
                # to begin counting from
                current_product = 1
                # set the contains zero flag to True
                contains_zero = True
            # else the number is non-zero
            else:
                # multiply the current product
                # by current number and keep track of it
                current_product *= num
                # update the max product if required with
                # the current product
                max_product = max(current_product, max_product)

        # finally, we will return the max product we found
        # in either direction, and if it contains 0 we will
        # return 0 if 0 > max_product
        return max_product if not contains_zero else max(max_product, 0)
