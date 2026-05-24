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

        # first we will create an array
        # where each index corresponds to
        # one of 26 lowercase letters
        # and the value is the count those
        # letters appear in s1
        s1_count_array = [0] * 26

        # then we will populate this array
        # with the frequencies of chars in s1
        # loop over all chars in s1
        for char in s1:
            # increment the respective frequencies
            # in the s1 count array
            s1_count_array[ord(char)-ord('a')] += 1

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
        
        # we can create a similar array to map
        # one of 26 lowercase letters as the index
        # to the count of those letters in the value
        # for our initial substring
        substring_count_array = [0] * 26

        # we can populate our substring count array
        # with the char frequencies of the
        # first initial substring 
        # loop through all indices for the first substring
        for i in range(start, end+1):
            # increment the respective frequencies
            # in the substring count array
            substring_count_array[ord(s2[i])-ord('a')] += 1
        
        # initially check if this first substring
        # is a permutation (meaning it has the same
        # char frequencies) of s1
        if substring_count_array == s1_count_array:
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
            substring_count_array[ord(s2[start])-ord('a')] -= 1

            # increment both the start and end pointers
            # moving our fixed sliding window 1 char to the right
            start += 1
            end += 1

            # after shifting the sliding window,
            # add the count of the rightmost char from
            # the new sliding window, since the rightmost
            # char is the new char added to the sliding window
            # each time we shift it from left to right
            substring_count_array[ord(s2[end])-ord('a')] += 1

            # check if this new substring from the new
            # sliding window is a permutation of s1
            # by checking if its char frequencies are the same
            # as the char frequencies of s1
            if substring_count_array == s1_count_array:
                # if they are, then return True immediately
                return True

        # if we get here, we have checked
        # all possible substring for permutations and not found
        # them, so return False
        return False
