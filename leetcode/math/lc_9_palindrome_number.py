'''
https://leetcode.com/problems/palindrome-number/description/
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # negative numbers cannot be palindromes
        if x < 0:
            # so we can immediately return false
            return False

        # first get the largest divider we can divide
        # by to get the left most digit
        divider = 1
        while x >= 10 * divider:
            divider *= 10

        # loop until we have chopped off all digits from x
        # which is when it becomes <= 0
        while x > 0:
            # get the right most digit
            right_digit = x % 10
            # get the left most digit
            left_digit = x // divider

            # if they are not the same, we can return False
            if right_digit != left_digit:
                return False

            # remove left digit to prep for next iteration
            x = x % divider
            # remove right digit to prep for next iteration
            x = x // 10

            # we removed two digits, so remove two digits
            # from our divider as well
            divider /= 100

        # if we get to this part, we know we have a palindrome.
        return True
