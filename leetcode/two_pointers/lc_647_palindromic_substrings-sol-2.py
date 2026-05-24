'''
https://leetcode.com/problems/palindromic-substrings/description/
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        # first handle the edge case
        # where we are given a string with 1 char
        if len(s) == 1:
            # just return directly
            return 1

        # init our palindrome count
        count = 0

        # loop through all indices in the string s
        for i in range(len(s)):
            # we will expand outward left and right from each index
            # and check that each new left and right char is the same
            # first check for ODD LENGTH palindromes
            # so init left and right to the same starting char
            left, right = i, i

            # loop as long as our left and right pointers
            # are in the range of s
            while 0 <= left and right < len(s):
                # if the two left and right chars are
                # the same, we have a valid palindrome
                if s[left] == s[right]:
                    # increment the palindrome count
                    count += 1
                # else the left and right chars are not the same
                # the palindrome is invalid
                else:
                    # break out of the while loop, no point
                    # iterating further
                    break

                # on each iteration, expand leftward
                left -= 1
                # and expand rightward
                right += 1

            # next check for EVEN LENGTH palindromes
            # so init left and right to 2 different starting chars
            left, right = i, i+1

            # loop as long as our left and right pointers
            # are in the range of s
            while 0 <= left and right < len(s):
                # if the two left and right chars are
                # the same, we have a valid palindrome
                if s[left] == s[right]:
                    # increment the palindrome count
                    count += 1
                # else the left and right chars are not the same
                # the palindrome is invalid
                else:
                    # break out of the while loop, no point
                    # iterating further
                    break

                # on each iteration, expand leftward
                left -= 1
                # and expand rightward
                right += 1

        # finally return the palindrome count
        return count
