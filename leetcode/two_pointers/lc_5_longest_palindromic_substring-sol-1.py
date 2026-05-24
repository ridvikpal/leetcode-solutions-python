'''
https://leetcode.com/problems/longest-palindromic-substring/description/
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # first handle the edge case
        # where we are given a string with 1 char
        # just return it directly
        if len(s) == 1:
            return s
        
        # init the left pointer for our palindrome
        palindrome_left = 0
        # init our right pointer for our palindrome
        palindrome_right = 0
        # at the start our max palindrome will be
        # the first char in the string s
        # so init our palindrome length to 1
        palindrome_length = 1

        # loop through all indices in the string s
        for i in range(len(s)):
            # we will expand outward left and right from each index
            # and check that each new left and right char is the same
            # first check for ODD LENGTH palindromes
            # so init left and right to the same starting char
            left, right = i, i
            # and the initial length of our palindrome to 1
            length = 1

            # loop as long as our left and right pointers
            # are in the range of s
            while 0 <= left and right < len(s):
                # if the two left and right chars are
                # the same, we have a valid palindrome
                if s[left] == s[right]:
                    # check if the length of our palindrome
                    # is greater than the saved palindrome we have
                    if length > palindrome_length:
                        # if it is, update the palindrome length
                        palindrome_length = length
                        # update the left pointer for our palindrome
                        palindrome_left = left
                        # update the right pointer for our palindrome
                        palindrome_right = right
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
                # and increment our length by 2 since
                # we add 2 chars to our palindrome each time
                length += 2

            # next check for EVEN LENGTH palindromes
            # so init left and right to 2 different starting chars
            left, right = i, i+1
            # and the initial length of our palindrome to 2
            length = 2

            # loop as long as our left and right pointers
            # are in the range of s
            while 0 <= left and right < len(s):
                # if the two left and right chars are
                # the same, we have a valid palindrome
                if s[left] == s[right]:
                    # check if the length of our palindrome
                    # is greater than the saved palindrome we have
                    if length > palindrome_length:
                        # if it is, update the palindrome length
                        palindrome_length = length
                        # update the left pointer for our palindrome
                        palindrome_left = left
                        # update the right pointer for our palindrome
                        palindrome_right = right
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
                # and increment our length by 2 since
                # we add 2 chars to our palindrome each time
                length += 2

        # finally return the largest palindrome we found
        # using string slicing
        return s[palindrome_left:palindrome_right+1]
