from typing import List


'''
https://leetcode.com/problems/product-of-array-except-self/description/
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # initialize our productArray with all 1s
        # all 1s because multiplying by 0 = 0
        productArray = [1] * len(nums)

        # First get all PREFIX PRODUCTS
        # reading the array from LEFT TO RIGHT
        # create a product variable to
        # keep track of the current product
        # begin the product at the first number
        product = nums[0]

        # loop through all numbers in the nums array
        # left to right excluding the first number
        for i in range(1, len(nums)):
            # set the current productArray element
            # to equal the product of the numbers before it
            # (aka. the prefix product)
            productArray[i] = product
            # update the product with the current number in nums
            product *= nums[i]

        # Second get all POSTFIX PRODUCTS
        # reading the array from RIGHT TO LEFT
        # reset our product variable at the last number
        product = nums[len(nums)-1]
        
        # loop through all numbers in the nums array
        # right to left, excluding the last number
        for i in range(len(nums)-2, -1, -1):
            # multiply the current productArray element
            # which includes the prefix product
            # with the product of the numbers after it
            # (aka. the postfix product)
            productArray[i] *= product
            # update the product with the current number in nums
            product *= nums[i]

        # finally return the product array
        return productArray
