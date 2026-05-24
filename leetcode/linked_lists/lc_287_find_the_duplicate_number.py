from typing import List


'''
https://leetcode.com/problems/find-the-duplicate-number/description/
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # note each nums[i] can be through of
        # as pointing to another index in the array
        # this means in the array (index, value)
        # index -> node
        # value -> points to another index (node)
        # making this a linked list cycle detection
        # problem, when two values are the same
        # so two different indexes have the same value
        # so two nodes point to each other
        # we can solve it using a modified version of
        # Floyd's algorithm for linked list cycle detection

        # create our slow pointer
        # increment it by 1 nodes (values)
        slow_pointer = nums[0]
        # create our fast pointer
        # increment it by 2 nodes (values)
        fast_pointer = nums[nums[0]]        

        # first loop through until the two 
        # slow and fast pointers equal one another
        # meaning we have arrived to the same
        # linked list nodes once
        while slow_pointer != fast_pointer:
            slow_pointer = nums[slow_pointer]
            fast_pointer = nums[nums[fast_pointer]]

        # now reset the slow pointer
        # and increment them 1 by 1 to ensure they can 
        # meet each other again
        # if they can meet each other again
        # then we know the previous time they met
        # was not a fluke and there is a cycle
        # this is because the fast pointer
        # will keep oscillating back and forth
        # in the cycle until the slow pointer catches 
        # up and equals it
        slow_pointer = 0
        while slow_pointer != fast_pointer:
            slow_pointer = nums[slow_pointer]
            fast_pointer = nums[fast_pointer]

        # now we know the value that is duplicated for sure
        # so return any of the slow or fast pointers
        return slow_pointer
