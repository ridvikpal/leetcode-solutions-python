from typing import List


'''
https://leetcode.com/problems/longest-common-prefix/description/
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # initialize our longest prefix
        longest_prefix = ''

        # begin comparing characters are index 0
        i = 0
        # We will init our comparision with the first
        # string in the array of strings, 
        # so loop until we are out of bounds
        while i < len(strs[0]):
            # get the character in the first string
            current_char = strs[0][i]
            # loop through all other strings
            # and check if the character exists in them
            # at the same index i
            for j in range(1, len(strs)):
                # check if:
                # 1) the index i is out of bounds of any
                #    of the other strings in strs
                # 2) the character at index i is not the same
                #    as the current_char in the first string
                if i >= len(strs[j]) or strs[j][i] != current_char:
                    # in any of these cases, there is no longer
                    # prefix, so return the longest prefix we found
                    return longest_prefix
            
            # add the current character to the longest prefix
            longest_prefix += current_char
            # increment the index i
            i += 1
    
        # finally, return the longest prefix we have found
        # to handle the edge case where we have 
        # list of all duplicate strings
        return longest_prefix
