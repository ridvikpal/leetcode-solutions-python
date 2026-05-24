from typing import List


'''
https://leetcode.com/problems/daily-temperatures/description/
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # first setup our stack
        # we will use a monotonic stack
        # where the stack will always be in decreasing
        # order because only smaller elements will
        # be inserted into it
        stack = []
        
        # setup our result array, initialized with all 0s
        result = [0] * len(temperatures)
        
        # loop through all indices in the temperatures array
        for i in range(len(temperatures)):
            # get the current temperature at this index
            temp = temperatures[i]

            # loop as long as there are elements in the stack
            # and current temp > top element in stack
            # i.e. we encounter a new greater temperature
            while stack and temp > stack[-1][1]:
                # pop the smaller element from the top of the stack
                # get it's previous index for that smaller value
                previous_i, _ = stack.pop()
                # for that previous index, it's value in 
                # results array is just difference between
                # current index for larger value and
                # the previous index for the smaller value
                result[previous_i] = i - previous_i

            # always append the new temperature to the stack
            stack.append((i, temp))

        # finally return the result array
        return result
