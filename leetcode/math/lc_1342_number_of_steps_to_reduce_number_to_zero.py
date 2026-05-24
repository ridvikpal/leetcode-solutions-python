'''
https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/
'''
class Solution:
    def numberOfSteps(self, num: int) -> int:
        # init our count variable to 0
        count = 0

        # loop as long as the number
        # is greater than 0
        while num > 0:
            # increment the count
            count += 1

            # check if the number is even
            if num % 2 == 0:
                # if it is, divide it by 2
                num /= 2
            # else the number is odd
            else:
                # then subtract 1 from it
                num -= 1

        # finally return the count
        return count
