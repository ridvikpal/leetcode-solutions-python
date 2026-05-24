'''
https://leetcode.com/problems/distinct-subsequences/description/
'''
class Solution:
    # we will use a top-down dynamic programming approach
    # where we memoize the result of a recursive function
    def numDistinct(self, s: str, t: str) -> int:
        # init our memoization 2d array
        # row will be s indices
        # cols will be t indices
        memoization = [[-1 for _ in range(len(t))] for _ in range(len(s))]

        # we can create our recursive function that will
        # return the the number of combinations of subsequences
        # of string s that can create string t
        # it takes in the char index1 of string s to look at
        # and the char index2 of string t to look at
        # we can use @cache to automatically memoize the result
        def search(index1, index2) -> int:
            # our first base case is if
            # we are out of bounds for index2
            # this means we have succesfully found
            # a combination because we have traversed t
            # fully
            if index2 >= len(t):
                # return 1 because we found 1 combination
                return 1

            # our second base case is if
            # we are out of bounds for index1
            # but are not out of bounds for index2
            # this means we have traversed s fully
            # and not been able to create t
            if index1 >= len(s):
                # so return 0 because we did not find
                # any combination
                return 0
            
            # first check if we have a memoized value stored
            if memoization[index1][index2] > -1:
                # if we do, simply return it
                return memoization[index1][index2]

            # otherwise, we can compare the chars
            # for both strings s and t at this indices
            # if they are the same
            if s[index1] == t[index2]:
                # if the chars are the same, we can
                # recursively search along 2 decisions:
                # 1) we skip this char in s to create our subsequence so 
                #    go to the next char in s but stay on the same char in t
                # 2) we use this char in s to create our subsequence so
                #    go to the next char in s and the next char in t
                # also make sure to store the result in our memoization dict
                memoization[index1][index2] = search(index1+1, index2) + search(index1+1, index2+1)
            # otherwise the chars are not the same
            else:
                # so we can only skip this char in s and stay on
                # the same char in t for our recursive search
                memoization[index1][index2] = search(index1+1, index2)
            
            # finally, we can return the memoized value we just stored
            return memoization[index1][index2]
            
        # finally, we can return the result
        # of our search function beginning at
        # index 0 for both s and t
        return search(0, 0)
