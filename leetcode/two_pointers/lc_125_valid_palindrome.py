'''
https://leetcode.com/problems/valid-palindrome/description/
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # setup our left pointer
        # to point to the first char
        left = 0
        # setup our right pointer
        # to point to the last char
        right = len(s)-1

        # loop as long as the left pointer
        # is smaller than the right pointer
        while left < right:
            # we will skip left chars that are not alpha numeric
            # so loop as long as left pointer < right pointer
            # and the left char is not alphanumeric
            while left < right and not s[left].isalnum():
                # increment left by 1 to skip the char
                left += 1

            # again, we will skip right chars that are not alpha numeric
            # so loop as long as the right pointer > left pointer
            # and the right char is not alphanumeric
            while right > left and not s[right].isalnum():
                # decrement by 1 to skip the char
                right -= 1

            # finally, perform the comparision between
            # the two alphanumeric chars if they are the same
            # make sure to convert to lowercase because palindromes
            # are case insensitive
            if s[left].lower() != s[right].lower():
                # if they are not the same, we can directly
                # return false -> it's not a palindrome
                return False

            # increment our left pointer to point to next left char
            left += 1
            # decrement our right pointer to point to next right char
            right -= 1

        # if we exit through the while loop we have
        # checked all chars and not found any palindrome violation
        # so return True
        return True
