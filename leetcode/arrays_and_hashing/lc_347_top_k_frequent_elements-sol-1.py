from collections import Counter
from typing import List


'''
https://leetcode.com/problems/top-k-frequent-elements/description/
'''
class Solution:
    # this is the O(n) solution, but arguably the heap
    # solution is easier to implement and only a bit slower.
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first use a counter to map each
        # each num -> it's count (aka. frequency) in the array
        nums_count = Counter(nums)

        # initialize our count_to_num array which
        # maps count (aka. frequency) as array index
        # to list of numbers with that count
        count_to_num = [[] for i in range(len(nums))]

        # loop through all the num, count pairs in our 
        # counter dictionary
        for num, count in nums_count.items():
            # set the count as aray index
            # and add the number to the list 
            # at that index
            # we do count-1 because arrays are 0 index
            # and no element will have 0 count in our array
            count_to_num[count-1].append(num)

        # initialize our result array
        result = []
        # initialize our count number
        # to keep track of how many elements 
        # in our result array
        count = 0

        # loop through our entire count_to_num array
        # in reverse because we want the elements with
        # the highest counts (largest indices) first
        for i in range(len(count_to_num)-1, -1, -1):
            # lopo through each element in the list
            # at each index of count_to_num
            for num in count_to_num[i]:
                # first check if our result array
                # contains k elements
                if count == k:
                    # if it does, then just return result
                    return result
                # otherwise, append the current number
                # to the result
                result.append(num)
                # and increment the count
                count += 1

        # for the edge case where k == len(nums)
        # and all numbers are distinct, then we
        # still need to return after all elements in 
        # count_to_num have been iterated through
        return result
