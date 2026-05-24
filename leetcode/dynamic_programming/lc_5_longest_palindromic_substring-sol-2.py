'''
https://leetcode.com/problems/longest-palindromic-substring/description/
'''
class Solution:
    # we will use dynamic programming with 
    # a bottom up tabular approach
    def longestPalindrome(self, s: str) -> str:
        # first handle the edge case where
        # we are given a string of length 1
        if len(s) == 1:
            # we can simply return the
            # single char directly
            return s

        # else init our max length as 1
        # because a single character is a palindrome
        max_length = 1
        # and set our left pointer to 0
        optimal_left = 0
        # and right pointer to 0, to make the first
        # char as our optimal palindrome
        optimal_right = 0

        # since we are using dynamic programming
        # we will setup our is palindrome memoization 2d array
        # which tells us if a palindrome beginning on row index
        # and ending at col index is a palindrome or not
        is_palindrome = [[0 for _ in range(len(s))] for _ in range(len(s))]

        # loop through all indices of the string
        # for our first pass to init our first base case
        # which is that a single char is a palindrome
        for i in range(len(s)):
            # init all single chars as palindromes
            # in our is palindrome array
            is_palindrome[i][i] = 1
        
        # loop through all indices of the string
        # except the last one for our second pass
        # to init our second base case which is
        # if two char substrings are palindromes
        for i in range(len(s)-1):
            # if the two adjacent chars are the same
            if s[i] == s[i+1]:
                # then mark them as palindromes
                is_palindrome[i][i+1] = 1
                # check if max length needs to be updated
                if max_length < 2:
                    # update max length accordingly
                    max_length = 2
                    # update optimal left pointer
                    optimal_left = i
                    # and optimal right pointer accordingly
                    optimal_right = i+1

        # now all base cases have been initalized
        # loop through all substrings with
        # length 3 to the full length of the string
        for length in range(3, len(s)+1):
            # for left pointer, loop through all
            # indices from 0 to string length - length of substring
            for left in range(len(s)-length+1):
                # set our right pointer to equal the left
                # pointer + the substring length
                # subtract 1 because arrays are 0-indexed
                right = left+length-1

                # check if the left and right chars are the same
                # and if the middle substring between the two chars
                # is a palindrome (which we already stored in our is palindrome array)
                # this will mean that our new substring with larger length
                # is also a palindrome
                if s[left] == s[right] and is_palindrome[left+1][right-1]:
                    # mark this new string as a palindrome
                    is_palindrome[left][right] = 1
                    # and update the max length if required
                    if length > max_length:
                        # update the max length
                        max_length = length
                        # update the optimal left pointer
                        optimal_left = left
                        # update the optimal right pointer
                        optimal_right = right
        
        # finally, return the longest substring using string slicing
        return s[optimal_left:optimal_right+1]
        