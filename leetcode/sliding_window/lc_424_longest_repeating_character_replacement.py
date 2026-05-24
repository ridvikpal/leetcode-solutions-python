from collections import defaultdict


'''
https://leetcode.com/problems/longest-repeating-character-replacement/description/
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # init our max substring length to be 1
        # because at the least the longest
        # substring is of length 1 with 1 char
        max_substring_length = 1

        # we will setup our start pointer
        # to point to index 0
        start = 0
        
        # we will use dictionary to keep
        # track of the count of each char
        # in our substring window
        char_count = defaultdict(int)

        # we start by updating the count
        # of our first character
        # (remember start=0) to 1
        char_count[s[start]] = 1

        # loop through all indices
        # skipping the first index 0
        for end in range(1, len(s)):
            # update the char count dictionary
            # with the new character pointed at by end
            char_count[s[end]] += 1

            # get the current substring length
            substring_length = end-start+1
            # get the current max char count,
            # the count of the character that occurs
            # most frequently in our substring
            max_char_count = max(char_count.values())

            # check if the substring length - max char count
            # is > k, the number of chars we can replace
            # if it is, then we don't have a valid substring
            # where we can have all the same chars after
            # k replacements, so we will iterate
            # to reduce the substring size until we do
            # have a valid substring
            while substring_length - max_char_count > k:
                # reduce the character count of the
                # character pointed at by start
                char_count[s[start]] -= 1
                # move the start pointer up 1 index
                start += 1
                # update the substring length, because
                # now it is smaller
                substring_length = end-start+1
                # update the max char count
                # because it could have also changed too
                max_char_count = max(char_count.values())

            # update the max substring length accordingly
            max_substring_length = max(substring_length, max_substring_length)

        # finally return the max substring length
        return max_substring_length
