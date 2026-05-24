from typing import Optional


'''
https://leetcode.com/problems/reverse-linked-list/description/
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # create current pointer to point
        # to the current node we want to reverse
        # in the linked list
        current = head

        # create a previous pointer to point
        # to the previous node in the linked list's
        # original order
        previous = None

        # create a next pointer to point
        # to the next node in the linked list's
        # original order
        next = None

        # loop as long as there are nodes
        # to reverse in the linked list
        # aka. until current pointer is not None
        while current:
            # store the next node in the next pointer
            next = current.next
            # update the current node's next pointer
            # to the prevoius node
            current.next = previous
            # set the previous node as the current node
            previous = current
            # and update the current node to the previously
            # saved next node
            current = next

        # finally, return the previous node
        # which will be the head at the end
        # of the reversal (because current will be None)
        return previous
