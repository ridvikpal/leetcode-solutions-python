from collections import Counter
from typing import List


'''
https://leetcode.com/problems/majority-element/description/
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # quickly return if there is only 1 element
        # in our array
        if len(nums) == 1:
            return nums[0]
        
        # otherwise count the occurance of each element
        # using a counter (can also do it manually using a dict)
        nums_count = Counter(nums)
        # return the first most common (majority) element
        return nums_count.most_common(1)[0][0]
