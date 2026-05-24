from collections import Counter
from typing import List


'''
https://leetcode.com/problems/top-k-frequent-elements/description/
'''
class Solution:
    # this is the O(nlog(k)) solution, easiest to implement
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the occurance of each number in the nums array
        # using a counter (really just a dictionary)
        counter = Counter(nums)

        # return the k most common elements in the dictionary
        return [x[0] for x in counter.most_common(k)]
