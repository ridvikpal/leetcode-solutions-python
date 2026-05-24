'''
https://leetcode.com/problems/palindromic-substrings/description/
'''
class Solution:
    # we will use a bottom up tabular dynamic programming approach
    def countSubstrings(self, s: str) -> int:
        # first handle the edge case where
        # we are given a string of length 1
        if len(s) == 1:
            # we can simply return 1 directly
            return 1

        # we can init our palindrome count to 0
        count = 0

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
            # and increment the count by 1
            count += 1
        
        # loop through all indices of the string
        # except the last one for our second pass
        # to init our second base case which is
        # if two char substrings are palindromes
        for i in range(len(s)-1):
            # if the two adjacent chars are the same
            if s[i] == s[i+1]:
                # then mark them as palindromes
                is_palindrome[i][i+1] = 1
                # and increment the count
                count += 1

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
                    # and increment the count
                    count += 1
        
        # finally return the palindrome count
        return count
