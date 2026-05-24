from collections import Counter


'''
https://leetcode.com/problems/permutation-in-string/description/
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # handle the edge case where
        # s2 is smaller in sizes than s1
        if len(s2) < len(s1):
            # in that case a permutation of s1
            # in s2 is impossible, so return False
            return False

        # first get mapping
        # of each char -> it's count
        # in the s1 string
        s1_counter = Counter(s1)

        # now we will begin checking
        # substrings that are of the
        # same size as s1 in s2
        # to begin, get the first substring
        # at the start of the s2 string
        # we will create a start pointer at index 0
        start = 0
        # and an end pointer at index len(s1)-1
        # our fixed sliding window size is len(s1)
        end = len(s1)-1
        
        # we can init our substring counter 
        # to start with the mapping of each
        # char -> it's count in the first substring
        substring_counter = Counter(s2[start:end+1])

        # initially check if this first substring
        # is a permutation (meaning it has the same
        # char frequencies) of s1
        if substring_counter == s1_counter:
            # if it does, then return True immediately
            return True

        # otherwise, we begin looping
        # until the end pointer = len(s2)-2
        # because in the loop we will increment it
        # by 1 to be len(s2)-1
        # in this loop we move our fixed sliding
        # window from left to right, 1 char at a time
        # and check if each created substring is a permutation
        while end < len(s2)-1:
            # on each iteration, first remove
            # the count of the leftmost char from 
            # the previous sliding window, since
            # the leftmost char is removed from
            # the sliding window each time we shift it
            # from left to right
            substring_counter[s2[start]] -= 1


            # increment both the start and end pointers
            # moving our fixed sliding window 1 char to the right
            start += 1
            end += 1

            # after shifting the sliding window,
            # add the count of the rightmost char from
            # the new sliding window, since the rightmost
            # char is the new char added to the sliding window
            # each time we shift it from left to right
            substring_counter[s2[end]] += 1

            # check if this new substring from the new
            # sliding window is a permutation of s1
            # by checking if its char frequencies are the same
            # as the char frequencies of s1
            if substring_counter == s1_counter:
                # if they are, then return True immediately
                return True

        # if we get here, we have checked
        # all possible substring for permutations and not found
        # them, so return False
        return False
