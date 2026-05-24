from typing import Optional


'''
https://leetcode.com/problems/add-two-numbers/description/
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # first we must get the first number
        multiplier = 1 # multiplier for each digits spot
        first_num = 0 # the first number is initialized to 0
        # traverse the linked list
        while l1:
            # increment the first number
            first_num += l1.val * multiplier
            # update the multiplier as we traverse the list
            multiplier *= 10
            # traverse the list by going to the next pointer
            l1 = l1.next

        # next we must get the second number
        # the exact same way as the first number
        # but traversing the second list
        multiplier = 1
        second_num = 0
        while l2:
            second_num += l2.val * multiplier
            multiplier *= 10
            l2 = l2.next

        # calculate the result
        result = first_num + second_num

        # handle edge case when result == 0
        if result == 0:
            return ListNode(0)

        # convert the result to a linked list
        # create a dummy head who's next pointer
        # will point to the actual head of the list
        current = dummyHead = ListNode()
        # loop until we have evaluated all digits
        # which is when the result will be <= 0
        while result > 0:
            # get the right digit
            right_digit = result % 10
            # update the result by removing
            # the right digit
            result = result // 10

            # create the linked list node for this digit
            current.next = ListNode(right_digit)
            # increment our current pointer to point to
            # newly created linked list node
            current = current.next

        # return the head using our dummyHead
        return dummyHead.next
