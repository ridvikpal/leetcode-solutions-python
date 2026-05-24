from typing import Optional


'''
https://leetcode.com/problems/linked-list-cycle/description/
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # we will use Floyd's cycle detection algorithm
    # for linked lists here
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # setup our fast and slow pointers
        # at the beginning of our linked list
        fast_pointer = slow_pointer = head

        # as long as the fast pointer
        # and it's next value exist
        # keep looping
        while fast_pointer and fast_pointer.next:
            # increment slow pointer by 1 node
            slow_pointer = slow_pointer.next
            # increment fast pointer by 2 nodes
            fast_pointer = fast_pointer.next.next

            # if they meet each other at some point
            # we have a cycle, so return true
            if fast_pointer == slow_pointer:
                return True

        # otherwise, fast_pointer eventually reaches None
        # before slow pointer and we don't have a cycle
        return False
